import array
import random
from random import SystemRandom, choice, choices
from secrets import choice, token_urlsafe
from string import digits, ascii_letters, punctuation
from sys import argv

filtered_punctuation = '~!@#$%^&*_£'

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

gen_pwd = ''.join(choice(characters[chartype])for i in range(n))
# gen_pwd = ''.join(choices(characters[chartype], k=n))

print(gen_pwd)
print(token_urlsafe(22))


def gen_random_string(char_set, length):
    if not hasattr(gen_random_string, "rng"):
        gen_random_string.rng = SystemRandom()  # Create a static variable
    return ''.join([gen_random_string.rng.choice(char_set) for _ in range(length)])


password_charset = ascii_letters + digits + filtered_punctuation
print(gen_random_string(password_charset, 22))


# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 22

# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<', '£', '`', '+', ';', ':', "'", ' ', '-']

# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
    password = password + x

# print out password
print(password)


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
