print("\n" + ">>>:"), print()#Space for convention only!
############################################



to_be_invited = ['Muhammad', 'Ahmad', 'Mansore']

invite_message = "You are invited to dinner tonight, don't be late.\"\n\nNabiL^^"

canceled_invitation = "Sorry, I can't make it"

print(f'{to_be_invited[0]}, "' + invite_message)
print(f'{to_be_invited[1]}, "' + invite_message)
print(f'{to_be_invited[2]}, "' + invite_message)

print(f"{to_be_invited[1]}: {canceled_invitation}")

rejected_the_invitation = to_be_invited.pop(1)
print(to_be_invited)

to_be_invited.insert(1, 'Mojeeb')
print(to_be_invited)

print(f'{to_be_invited[0]}, "' + invite_message)
print(f'{to_be_invited[1]}, "' + invite_message)
print(f'{to_be_invited[2]}, "' + invite_message)

print("We found a bigger table. We need more people!")

to_be_invited.insert(0, 'Mustafa')
to_be_invited.insert(2, 'Abraham')
to_be_invited.append('Najeeb')

print(to_be_invited)

print(f'{to_be_invited[0]}, "' + invite_message)
print(f'{to_be_invited[1]}, "' + invite_message)
print(f'{to_be_invited[2]}, "' + invite_message)
print(f'{to_be_invited[3]}, "' + invite_message)
print(f'{to_be_invited[4]}, "' + invite_message)
print(f'{to_be_invited[5]}, "' + invite_message)

apologize_message = "Dinner table did not arrive so I can only invite two people!"

removed = to_be_invited.pop()
print(f"{removed} Sorry I can't invite you today. {apologize_message}" )
removed = to_be_invited.pop()
print(f"{removed} Sorry I can't invite you today. {apologize_message}" )
removed = to_be_invited.pop()
print(f"{removed} Sorry I can't invite you today. {apologize_message}" )
removed = to_be_invited.pop(); 
print(f"{removed} Sorry I can't invite you today. {apologize_message}" )

print(to_be_invited)

print(f'{to_be_invited[0]}, You\'re still invited')
print(f'{to_be_invited[1]}, You\'re still invited')


del to_be_invited[0]
del to_be_invited[0]

print(to_be_invited)


############################################
print('\n') #Space for convention only!