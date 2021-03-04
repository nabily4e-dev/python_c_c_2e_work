
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################



copy_of_messages = []
messages = ['good morining', 'have a nice day', 'good evening']
sent_messages = []


def send_messages(messages, sent_messages):
    """Sending messages and have a cop of each one!"""

    if messages:
        for i in messages:
            copy_of_messages.append(i)

        while messages:
            current_message = messages.pop()
            print(current_message)
            sent_messages.append(current_message)

    else:
        print("Can't print, the list is empty")


def show_messages(messages):
    """"Showing simple messages"""
    
    if messages:
        for message in messages:
            print(message.title())
    else:
        print("Can't print, the list is empty")


send_messages(messages[:], sent_messages)
show_messages(messages)

print(messages, sent_messages, copy_of_messages)




############################################
print('\n')  # Spaces for convention only!
############################################
