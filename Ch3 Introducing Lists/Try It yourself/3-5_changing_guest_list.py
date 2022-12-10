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



############################################
print('\n') #Space for convention only!