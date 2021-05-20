############################################
import json
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/favorite_number.json'


try:
    with open(filename)as f:
        contents = json.load(f)
except FileNotFoundError:
    print(f"Can't find {filename}")
else:
    print(f"I know your favorite number! It’s {contents}.")


############################################
print('\n')  # Spaces for convention only!
############################################
