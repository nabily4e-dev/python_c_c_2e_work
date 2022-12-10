############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################


filenames = ['/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/cats.txt',
             '/home/nabily4e/Desktop/Python crash course/python_c_c_2e_work/Ch10 Files and Eceptions/Try It Yourself/dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)

    except FileNotFoundError:
        print("  Sorry, I can't find that file.")


############################################
print('\n')  # Spaces for convention only!
############################################
