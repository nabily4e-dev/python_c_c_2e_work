import json

filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
