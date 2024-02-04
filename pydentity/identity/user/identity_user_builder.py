from .identity_user import IdentityUser
from .i_identity_user_builder import IIdentityUserBuilder


class IdentityUserBuilder(IIdentityUserBuilder):

    def __init__(self) -> None:
        self._user = None
        self.reset()

    def reset(self) -> None:
        self._user = IdentityUser()

    def build_user(self):
        user = self._user
        self.reset()
        return user

    def with_user_id(self, user_id):
        self._user.user_info["user_id"] = user_id
        return self

    def with_user_first_name(self, first_name):
        self._user.user_info["first_name"] = first_name
        return self

    def with_user_last_name(self, last_name):
        self._user.user_info["last_name"] = last_name
        return self

    def with_user_username(self, username):
        self._user.user_info["username"] = username
        return self

    def with_user_discriminator(self, discriminator):
        self._user.user_info["discriminator"] = discriminator
        return self

    def with_user_avatar(self, avatar):
        self._user.user_info["avatar"] = avatar
        return self

    def with_user_locale(self, locale):
        self._user.user_info["locale"] = locale
        return self

    def with_user_email(self, email):
        self._user.user_info["email"] = email
        return self

    def with_user_email_verified(self, email_verified=False):
        self._user.user_info["email_verified"] = email_verified
        return self

    def with_user_created_at(self, created_at):
        self._user.user_info["created_at"] = created_at
        return self

    def with_user_logins(self, logins):
        self._user.user_info["logins"] = logins
        return self

    def with_user_roles(self, roles=None):
        if roles is None:
            roles = []
        self._user.user_info["roles"] = roles
        return self

    def with_user_lockout_end(self, lockout_end=None):
        self._user.user_info["lockout_end"] = lockout_end
        return self

    def with_user_lockout_enabled(self, lockout_enabled=False):
        self._user.user_info["lockout_enabled"] = lockout_enabled
        return self

    def with_user_access_failed_count(self, access_failed_count=0):
        self._user.user_info["access_failed_count"] = access_failed_count
        return self
