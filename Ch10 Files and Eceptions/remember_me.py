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


def get_new_user():
    """Prompt for a new username."""

    filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/username.json'
    username = get_stored_username()

    with open(filename, 'w')as f:
        json.dump(username, f)

    return username


def greet_user():
    """Greet user by name."""

    username = get_stored_username()

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user()
        print(f"We'll remember you when you come back, {username}!")


greet_user()


############################################
print('\n')  # Spaces for convention only!
############################################
