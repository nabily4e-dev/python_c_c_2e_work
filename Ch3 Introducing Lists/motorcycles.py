print("\n" + ">>>:"), print()#Space for convention only!
############################################




motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []; print(motorcycles)
motorcycles.append('honda'), print(motorcycles)
motorcycles.append('yamaha'), print(motorcycles)
motorcycles.append('suzuki'), print(motorcycles)
print(motorcycles[-1])


motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati'), print(motorcycles)
# motorcycles.insert(-1, '#####'), print(motorcycles)
# motorcycles.insert(55, 'my_brand!'), print(motorcycles)
# motorcycles.insert(-1, '#####'), print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.append('suzuki')
print(motorcycles)
last_owned = motorcycles.pop()
print(f"The last motorcycle I ever owned was a {last_owned.title().capitalize()}.")

last_owned = motorcycles.pop(0)
print(f"The first motorcycle I ever owned was a {last_owned.title().capitalize()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")






# The output needs to be understood(confusing)!
print(motorcycles.remove('yamaha'))
motorcycles = motorcycles
print(motorcycles)





############################################
print('\n') #Space for convention only!