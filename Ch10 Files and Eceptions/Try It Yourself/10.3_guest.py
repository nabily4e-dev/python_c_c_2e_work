############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)


############################################
print('\n')  # Spaces for convention only!
############################################
