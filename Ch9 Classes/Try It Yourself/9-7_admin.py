############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


class User:
    """Simple representation of a user profile"""
    def __init__(
        self,
        id,
        first_name,
        last_name,
        username,
        email,
        address,
    ):
        """Initialize attributes to represent a user profile"""

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.address = address
        self.login_attempts = 0

    def describe_user(self):
        """Printing user's info"""

        print(f"User Id: {self.id}")
        print(f"Username: {self.username}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")

    def greet_user(self):
        """A simple message to greet user"""

        full_name = self.first_name + " " + self.last_name

        print(f"{full_name.title()}, Hello and welcome")

    def increment_login(self):
        """Incrementing the number of login attempts."""

        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resitting the login attempts attribute."""

        self.login_attempts = 0


class Privileges:
    """"""
    def __init__(self):
        """"""

        self.privileges = ['can add post', 'can delete post', 'can ban users']
        
    def show_privileges(self):
        """"""

        print("Privileges to controll:")
        for privilege in self.privileges:
            print('\t', privilege)
            

class Admin(User):
    """"""
    def __init__(
        self,
        id,
        first_name,
        last_name,
        username,
        email,
        address,
    ):
        """"""

        super().__init__(
            id,
            first_name,
            last_name,
            username,
            email,
            address,
        )

        self.privileges = Privileges()

    # def show_privileges(self):
    #     """"""

    #     print("Privileges to controll:")
    #     for privilege in self.privileges:
    #         print('\t', privilege)





admin = Admin(1, 'NabiL', 'Khalid', 'nabily4e', 'napil101@gmail.com', "Sana'a")

print(admin.privileges.show_privileges())



############################################
print('\n')  # Spaces for convention only!
############################################
