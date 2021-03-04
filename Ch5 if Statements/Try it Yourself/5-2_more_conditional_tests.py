print("\n\n\n\n\n" + ">>>:"), print() # Spaces for convention only!
############################################


if 2 > 1:
    print("This is a True statement!")


var1 = 1
var2 = 3
if var1 > var2:
    print("This is also True")


if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

print('After conditional')


print(3 == 5)
print(3 > 5)
print(3 <=5)
print(len("ATGC") > 5)
print("GAATTC".count("T") > 1)
print("ATGCTT".startswith("ATG"))
print("ATGCTT".endswith("TTT"))
print("ATGCTT".isupper())
print("ATGCTT".islower())
print("V" in ["V", "W", "L"])

print(True)
print(False)

expression_level = 125
if expression_level > 100:
    print("gene is highly expressed")


accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        print(accession)






############################################
print('\n') #Spaces for convention only!