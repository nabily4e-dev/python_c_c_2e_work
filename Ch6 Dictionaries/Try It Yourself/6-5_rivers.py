
############################################
from typing import Counter


print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




rivers = {
    'nile':
    'egypt',
    'benue':
    'cameroon',
    'chelif':
    'algeria',
}

if rivers:
    for river, country in rivers.items():
        print(f"The {river.title()} runs through {country.title()}")

if rivers:
    for key in rivers.keys():
        print(key)

if rivers:
    for key in rivers.values():
        print(key)




############################################
print('\n')  # Spaces for convention only!
############################################
