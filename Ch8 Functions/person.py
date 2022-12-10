
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""

    person = {'first': first_name, 'last': last_name}

    return person


musician = build_person('jimi', 'handrix')
print(musician)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person

    
musician = build_person('jimi', 'hendrix', age=27)
print(musician)



############################################
print('\n')  # Spaces for convention only!
############################################
