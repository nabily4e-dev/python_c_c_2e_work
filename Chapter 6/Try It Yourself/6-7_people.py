
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################



users = {
    'ali123': {
        'first_name': 'ali',
        'last_name': 'daaer',
        'age': 22,
        'length': 154,
        'city': 'sana\'a',
    },

    'muhammad123': {
        'first_name': 'muhammad',
        'last_name': 'Zahrani',
        'age': 18,
        'length': 166,
        'city': 'sana\'a',
    },

    'khalid123': {
        'first_name': 'khalid',
        'last_name': 'ashbat',
        'age': 48,
        'length': 170,
        'city': 'sana\'a',
    }

}

person_1 = {
    'first_name': 'ali',
    'last_name': 'daaer',
    'age': 22,
    'length': 154,
    'city': 'sana\'a'
    }

person_2 = {
    'first_name': 'muhammad',
    'last_name': 'zahrani',
    'age': 18,
    'length': 166,
    'city': 'sana\'a',
}

person_3 = {
    'first_name': 'khalid',
    'last_name': 'ashbat',
    'age': 48,
    'length': 170,
    'city': 'sana\'a',
}

people = [person_1, person_2, person_3]

title = []

if people:
    for person in people:
        full_name = f"{person['first_name']} {person['last_name']}"
        age = f"{person['age']}"
        length = f"{person['length']}"
        city = f"{person['city']}"

        for value in person:
            title.append(value.title())

        print(f"Full name: {full_name.title()}.")
        print(f"\tAge: {age.title()}.")
        print(f"\tLength: {length.title()}.")
        print(f"\tCity: {city.title()}\n")

#print(title)

############################################
print('\n')  # Spaces for convention only!
############################################
