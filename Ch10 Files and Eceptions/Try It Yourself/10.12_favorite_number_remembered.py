############################################
import json
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/favorite_number.json'


try:
    with open(filename)as f:
        contents = json.load(f)
except FileNotFoundError:
    try:
        fav_num = input("What is your favorite number? ")
        fav_num = int(fav_num)

    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        with open(filename, 'w')as f:
            json.dump(fav_num, f)
else:
    print(f"I know your favorite number! It’s {contents}.")


# try:
#     with open('favorite_number.json') as f:
#         number = json.load(f)
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     with open('favorite_number.json', 'w') as f:
#         json.dump(number, f)
#     print("Thanks, I'll remember that.")
# else:
#     print(f"I know your favorite number! It's {number}.")


############################################
print('\n')  # Spaces for convention only!
############################################
