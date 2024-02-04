from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from .identity_user import IdentityUser


class IIdentityUserBuilder(ABC):
    @abstractmethod
    def build_user(self) -> IdentityUser:
        pass

    @abstractmethod
    def with_user_id(self, user_id: Any) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_first_name(self, first_name: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_last_name(self, last_name: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_username(self, username: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_discriminator(self, discriminator: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_avatar(self, avatar: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_locale(self, locale: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_email(self, email: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_email_verified(self, email_verified: bool) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_created_at(self, created_at: str) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_logins(self, logins: list) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_roles(self, roles: list) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_lockout_end(self, lockout_end: str) -> IIdentityUserBuilder:
        pass

    def with_user_lockout_enabled(self, lockout_enabled: bool) -> IIdentityUserBuilder:
        pass

    @abstractmethod
    def with_user_access_failed_count(self, access_failed_count: int) -> IIdentityUserBuilder:
        pass
