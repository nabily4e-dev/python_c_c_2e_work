
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




sandwich_orders = ['falafel', 'peperoni', 'motabaqia']
finished_sandwitchs = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwitch = sandwich_orders.pop()

    finished_sandwitchs.append(finished_sandwitch)

while sandwich_orders:
    finished_sandwitch = sandwich_orders.pop()
    print(f"I made your {finished_sandwitch} sandwich.")

    finished_sandwitchs.append(finished_sandwitch)

    


############################################
print('\n')  # Spaces for convention only!
############################################
