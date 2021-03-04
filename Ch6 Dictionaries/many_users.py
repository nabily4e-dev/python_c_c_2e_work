
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'paris',
    },

    'mcuire': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}


# if users:
#     for username, user_info in users.items():
#         print(f"Username: {username.title()}")
#         for key, value in user_info.items():
#             print(f"Full name: {value.title()} {key.title()}")


if users:
    for username, user_info in users.items():
        print(f"Username: {username.title()}")
         
        full_name = f"{user_info['last']} {user_info['first']}"
        location = f"{user_info['location']}"

        print(f"\tFull name: {full_name.title()}\n\t"
            "Location: {location.title()}\n")




############################################
print('\n')  # Spaces for convention only!
############################################
