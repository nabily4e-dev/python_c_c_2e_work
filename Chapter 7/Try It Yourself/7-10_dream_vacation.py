
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




dream_vacation = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    dream_vacation[name] = place

    repeat = input("Would like to lest another person response? (yes / no) ")

    if repeat == 'no':
        polling_active = False

for name, place in dream_vacation.items():
    print(f"{name.title()} want to visit: {place.title()}.")


############################################
print('\n')  # Spaces for convention only!
############################################
