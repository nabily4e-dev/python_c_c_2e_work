############################################
import json
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


def get_stored_username():
    """Get stored username if available."""

    filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/username.json'

    try:
        with open(filename)as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""

    filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/username.json'
    username = input("What is your name? ")

    with open(filename, 'w')as f:
        json.dump(username, f)

    return username


def greet_user():
    """Greet user by name."""

    username = get_stored_username()

    if username:
        correct_username = input(f"Is this {username} your name? (y/n) ")
        if correct_username == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


 # A cleaner version of greet_user():
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    # Let's prompt for a new username.
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


greet_user()


############################################
print('\n')  # Spaces for convention only!
############################################
