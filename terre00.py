#Init the var
alphabet = ""

#We iterate on the numbers of the ascii table from letter A to Z
for x in range(ord('a'),ord('z')+1):
    alphabet += chr(x)  #Converting int to char adding it to the alphabet
    x += 1

#Display the var alphabet with all the chars
print(alphabet)
