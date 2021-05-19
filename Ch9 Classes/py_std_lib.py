from random import choices
from secrets import choice

from string import digits, ascii_letters, punctuation
from sys import argv

filtered_punctuation = '~!@#$%^&*_'

if len(argv) == 3:
    chartype = args[1]
    n = int(args[2])
else:
    prompt = 'Password characters:\n (D)igits\n (L)etters\n (S)ymbols\n (A)ll\n (W)ithout Ambiguous Characters\n'
    chartype = input(prompt)
    n = int(input("Length? "))
    chartype = chartype.lower()[0]

characters = {
    'd': digits,
    'l': ascii_letters,
    's': punctuation,
    'a': digits + ascii_letters + punctuation,
    'w': digits + ascii_letters + filtered_punctuation,
}

# gen_pwd = ''.join(choice(characters[chartype])for i in range(n))
gen_pwd = ''.join(choices(characters[chartype], k=n))

print(gen_pwd)


# choice = 1
# pwd_length = 20

# digits = digits
# l_letters = ascii_lowercase
# u_letters = ascii_uppercase
# symbols = punctuation
# all_characters = ascii_letters

# generated_password = None

# if(choice > 0):
#     if(choice == 1):
#         for number in range(pwd_length+1):
#             generated_password += choice(digits)
#     elif(choice == 2):
#         for l_letter in range(pwd_length+1):
#             generated_password.append(random.choice(l_letters))
#     elif(choice == 3):
#         for u_letter in range(pwd_length+1):
#             generated_password.append(random.choice(u_letters))
#     elif(choice == 4):
#         for symbol in range(pwd_length+1):
#             generated_password.append(random.choice(symbols))
#     elif(choice == 'all' or 'All'):
#         for i in range(length+1):
#             password += random.choice(characters)
# else:
#     print('Wrong input!')


# print(generated_password)

# print(random.randint(1, 6))

# print(random.choice(['charles', 'martina', 'eli']))
