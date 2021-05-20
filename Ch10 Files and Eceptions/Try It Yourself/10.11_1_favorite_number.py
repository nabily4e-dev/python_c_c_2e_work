############################################
import json
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/favorite_number.json'

fav_num = input("What is your favorite number? ")

try:
    with open(filename, 'w')as f:
        json.dump(fav_num, f)
except FileNotFoundError:
    print(f"Can't find {filename}")
else:
    print("Thanks!, we will remember it for you.")


############################################
print('\n')  # Spaces for convention only!
############################################
