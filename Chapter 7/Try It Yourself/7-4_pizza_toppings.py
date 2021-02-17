
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




prompt = "\nTell me what topping you want your pizza with?"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"I'll add {message.title()} topping to the pizza!")



############################################
print('\n')  # Spaces for convention only!
############################################
