
############################################
print("\n\n\n\n\n" + ">>>:"), print()  # Spaces for convention only!
############################################



def make_sandwitch(*sandwitches):

    if sandwitches:
        for sandwitch in sandwitches:
            print(f"The {sandwitch} sandwitch has been ordered!")


# print(f"////////////////////\nThe" + make_sandwitch('falafel') + "sandwitch has been ordered!\n////////////////////")

print("////////////////////")
make_sandwitch('falafel')
print("\n////////////////////")
make_sandwitch('finger', 'zinger')
print("\n////////////////////")
make_sandwitch('falafel', 'finger', 'zinger')



############################################
print('\n')  # Spaces for convention only!
############################################
