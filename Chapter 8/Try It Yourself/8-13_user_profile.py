
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################

# Parameter ==> (   --argument_1--, --argument_2--, ...   )



def build_profile(first, last, **user_info):
    """Adding user info..."""
    
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info


user_info = build_profile('nabil', 'ashbat',
                            language='arabic', country='yemen')

print(user_info)



############################################
print('\n')  # Spaces for convention only!
############################################
