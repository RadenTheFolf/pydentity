import asyncio
from functools import wraps
import abc
import contextvars

base_method_called_var = contextvars.ContextVar('base_method_called', default=False)

def force_super_call(method):
    if asyncio.iscoroutinefunction(method):
        @wraps(method)
        async def checker_wrapper(*args, **kwargs):
            base_method_called_var.set(False)
            try:
                result = await method(*args, **kwargs)
            finally:
                base_method_called_var.set(True)
            return result

        async def client_decorator(leaf_method):
            @wraps(leaf_method)
            async def client_wrapper(*args, **kwargs):
                base_method_called_var.set(False)
                try:
                    result = await leaf_method(*args, **kwargs)
                finally:
                    if not base_method_called_var.get():
                        raise RuntimeError(f"Overriden method '{method.__name__}' did not cause the base method to be called")
                    base_method_called_var.set(False)
                return result
            return client_wrapper
    else:
        @wraps(method)
        def checker_wrapper(*args, **kwargs):
            base_method_called_var.set(False)
            try:
                result = method(*args, **kwargs)
            finally:
                base_method_called_var.set(True)
            return result

        def client_decorator(leaf_method):
            @wraps(leaf_method)
            def client_wrapper(*args, **kwargs):
                base_method_called_var.set(False)
                try:
                    result = leaf_method(*args, **kwargs)
                finally:
                    if not base_method_called_var.get():
                        raise RuntimeError(f"Overriden method '{method.__name__}' did not cause the base method to be called")
                    base_method_called_var.set(False)
                return result
            return client_wrapper

    checker_wrapper.client_decorator = client_decorator
    return checker_wrapper

def forcecall__getattribute__(self, name):
    cls = type(self)
    method = object.__getattribute__(self, name)
    registry = type(cls).forcecall_registry
    for superclass in cls.__mro__[1:]:
        if superclass in registry and name in registry[superclass]:
            method = registry[superclass][name](method)
            break
    return method

class ForceBaseCallMeta(abc.ABCMeta):
    forcecall_registry = {}

    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        mcls.forcecall_registry[cls] = {}
        for name, method in cls.__dict__.items():
            if hasattr(method, "client_decorator"):
                mcls.forcecall_registry[cls][name] = method.client_decorator
        cls.__getattribute__ = forcecall__getattribute__
        return cls