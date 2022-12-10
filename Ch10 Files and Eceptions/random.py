
filename = '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/random.txt'

while True:
    with open(filename, 'a') as f:
        f.write("Welcome Home!\n")
