from __future__ import annotations

from .i_identity_user_builder import IIdentityUserBuilder


class IdentityUserManager:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> IIdentityUserBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: IIdentityUserBuilder):
        self._builder = builder

    def build_user_from_dict(self, data: dict = None):
        if self.builder is None:
            raise ValueError("No builder set")

        if data is None:
            raise ValueError("No data provided")

        if "user_id" in data:
            self.builder.with_user_id(data["user_id"])
        if "first_name" in data:
            self.builder.with_user_first_name(data["first_name"])
        if "last_name" in data:
            self.builder.with_user_last_name(data["last_name"])
        if "username" in data:
            self.builder.with_user_username(data["username"])
        if "discriminator" in data:
            self.builder.with_user_discriminator(data["discriminator"])
        if "avatar" in data:
            self.builder.with_user_avatar(data["avatar"])
        if "locale" in data:
            self.builder.with_user_locale(data["locale"])
        if "email" in data:
            self.builder.with_user_email(data["email"])
        if "email_verified" in data:
            self.builder.with_user_email_verified(data["email_verified"])
        if "created_at" in data:
            self.builder.with_user_created_at(data["created_at"])
        if "logins" in data:
            self.builder.with_user_logins(data["logins"])
        if "roles" in data:
            self.builder.with_user_roles(data["roles"])
        if "lockout_end" in data:
            self.builder.with_user_lockout_end(data["lockout_end"])
        if "lockout_enabled" in data:
            self.builder.with_user_lockout_enabled(data["lockout_enabled"])
        if "access_failed_count" in data:
            self.builder.with_user_access_failed_count(data["access_failed_count"])

        return self.builder.build_user()

