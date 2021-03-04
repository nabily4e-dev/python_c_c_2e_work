
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################




prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the program. " 

# message = ""
# while message != 'quit':
#     message = int(input(prompt))

#     if message < 3:
#         print("The ticket is free")
#     elif message <= 12:
#         print("The ticket is 10$")
#     else:
#         print("The ticket is 15$")


while True:
    message = int(input(prompt))

    if str(message) == 'quit':
        break

    if message < 3:
        print("The ticket is free")
    elif message <= 12:
        print("The ticket is 10$")
    else:
        print("The ticket is 15$")


############################################
print('\n')  # Spaces for convention only!
############################################
