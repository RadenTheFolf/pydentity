from pydentity.identity.user import IdentityUserManager, IdentityUserBuilder

if __name__ == '__main__':
    testmgr = IdentityUserManager()
    testmgr.builder = IdentityUserBuilder()
    user = testmgr.build_user_from_dict({
        "user_id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "discriminator": "0001",
        "avatar": "https://example.com/avatar.jpg",
        "locale": "en-US",
        "email": "test@example.com",
        "email_verified": True,
        "created_at": "2021-01-01T00:00:00Z",
        "logins": [{"login_provider": "example", "provider_key": "example"}],
        "roles": ["user"]
    })
    print(user.user_info)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
