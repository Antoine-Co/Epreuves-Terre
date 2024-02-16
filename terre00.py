
alphabet = ""

#We iterate on the numbers of the ascii table
for x in range(ord('a'),ord('z')+1):
    alphabet += chr(x) #converting int to char adding to alphabet
    x += 1

print(alphabet)
