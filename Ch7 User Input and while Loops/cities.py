############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




prompt = "\nlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")



############################################
print('\n')  # Spaces for convention only!
############################################
