print("\n" + ">>>:"), print()#Space for convention only!
############################################


cars =['bmw', 'audi', 'toyota', 'subaru']
print("Before: \n", cars)
cars.sort()
print("After: \n", cars)

print(), print()

cars =['bmw', 'audi', 'toyota', 'subaru']
print("Before: \n", cars)
cars.sort(reverse=True)
print("After: \n", cars)

print(), print()

cars =['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reversed list:")
#print(sorted(cars.reverse()))
print("\nHere is the original list again:")
print(cars)

print(), print()

cars =['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
sorted_list = sorted(cars).reverse()
sorted_list_2 = sorted(cars)
print("\nHere is the sorted list:")
print(sorted_list)
print(sorted_list_2.reverse())
print(reversed(sorted_list_2))
print("\nHere is the original list again:")
print(cars)

print(), print()

print(len(cars))




############################################
print('\n') #Space for convention only!