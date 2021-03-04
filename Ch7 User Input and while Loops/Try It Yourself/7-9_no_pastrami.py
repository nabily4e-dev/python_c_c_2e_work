
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




sandwich_orders = ['pastrami', 'falafel', 'pastrami', 'peperoni', 'motabaqia', 'pastrami']

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("What we have availabe today:")
for sandwich_order in sandwich_orders:
    print(f"\t{sandwich_order}")




############################################
print('\n')  # Spaces for convention only!
############################################
