
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




def get_formatted_name(first_name, last_name):
    """"Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name('jimi', 'handrix')
print(musician)


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

musician = get_formatted_name('john', 'hooker')
print(musician)




############################################
print('\n')  # Spaces for convention only!
############################################
