
############################################
from typing import Counter


print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


people = ['jen', 'phil', 'ban', 'jim']

if favorite_languages and people:
    for poll in favorite_languages:
        if poll in people:
            print(f"{poll.title()}, thanks for responding.")
        else:
            print(f"{poll.title()}, please take the poll!.")




############################################
print('\n')  # Spaces for convention only!
############################################
