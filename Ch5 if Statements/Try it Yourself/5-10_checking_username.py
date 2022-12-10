print("\n\n\n\n\n" + ">>>:"), print() # Spaces for convention only!
############################################




current_users = ['Ahmad', 'Muhammad', 'Anower', 'Miriam', 'Nermin']

lower_case_users = []

for name in current_users:
    lower_case_users.append(name.lower())


new_users = ['Mojeep', 'Loai', 'Mansoor', 'Ahmad', 'muhammad']

if new_users:
    for new_user in new_users:
        if new_user in current_users or new_user in lower_case_users:
            print("You will need to enter a new username.")
        else:
            print("The username is available.")



############################################
print('\n') #Spaces for convention only!

