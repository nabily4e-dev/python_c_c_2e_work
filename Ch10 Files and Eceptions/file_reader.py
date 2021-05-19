# with open('alice.txt') as fb:
#     contents = fb.read()
# print(contents)

# print(), print()

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# with open('/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# with open('./pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

filename = 'pi_digits.txt'

with open(filename)as file_object:
    for line in file_object:
        print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
