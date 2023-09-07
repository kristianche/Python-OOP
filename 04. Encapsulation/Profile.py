class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        if 5 <= len(new_username) <= 15:
            self.__username = new_username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        elif new_password.lower() == new_password:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        elif not [i for i in new_password if i.isdigit()]:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = new_password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

