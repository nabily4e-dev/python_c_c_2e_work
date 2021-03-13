
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################

# Parameter ==> (   --argument_1--, --argument_2--, ...   )


def build_profile(first, last, **user_info):
    """Build a dictionary containing verything we know a bout the user."""

    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info


user_profile = build_profile('alert', 'einstein', 
                                location='princeton', field='physics')

for key, value in user_profile.items():
    print(f"{key}: {value}")


print(user_profile)





############################################
print('\n')  # Spaces for convention only!
############################################
