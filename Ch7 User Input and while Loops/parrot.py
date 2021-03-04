
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit \ q' to end the program. "

active = True
while active:
    message = input(prompt)

    if message != 'quit':
        print(message)
    else:
        active = False




############################################
print('\n')  # Spaces for convention only!
############################################
