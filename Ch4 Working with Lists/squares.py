print("\n" + ">>>:"), print()#Space for convention only!
############################################


squares = []

for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)

    squares.append(value ** 2)

print(squares, "\n\n")


digits = list(range(1, 10)) + [] # ==> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits, '\n\n', 'Minimum number:',
min(digits), ' |  Maximum number:',
max(digits), ' |  Summition:',
sum(digits), '\n\n')

squares = [value ** 2 for value in range(1, 11)]
print(squares, '\n\n')



############################################
print('\n') #Space for convention only!