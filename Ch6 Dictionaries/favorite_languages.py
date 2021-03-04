
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', # Best practice
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())


# favorite_languages = {

# }

# print(favorite_languages)

# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

print(), print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    #'erin': 'c++',
    }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print('Hi',name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(f"{name}, Thanks for taking the poll.")


print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# Sets
languages = {'python', 'c', 'ruby', 'python',}

print(languages)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}


if favorite_languages:
    for name, languages in favorite_languages.items():
        if len(languages) is 1:
            print(f"{name.title()}'s favorite language is:")
        else:
            print(f"{name.title()}'s favorite languages are:")

        for language in languages:
            print(f"\t{language.title()}")



############################################
print('\n')  # Spaces for convention only!
############################################
