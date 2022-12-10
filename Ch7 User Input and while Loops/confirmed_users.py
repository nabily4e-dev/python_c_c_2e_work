
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################



unconfirmed_users = ['alice', 'brain', 'candance']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying users: {current_user.title()}")
    confirmed_users.append(current_user)

print(confirmed_users, unconfirmed_users)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())




############################################
print('\n')  # Spaces for convention only!
############################################
