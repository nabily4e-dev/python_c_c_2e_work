############################################
import json
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


numbers = [2, 3, 5, 7, 11, 13]

filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/numbers.json'

with open(filename, 'w')as f:
    json.dump(numbers, f)


############################################
print('\n')  # Spaces for convention only!
############################################
