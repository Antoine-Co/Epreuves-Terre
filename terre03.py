import sys

firstArg = sys.argv[1]

#Check len arg -> only char of len=1
#Check if the arg is a letter
if (len(firstArg) > 1 or not firstArg.isalpha()):
    print("Dsl il faut une seule lettre en argument.")
elif (len(sys.argv) > 2): #Check the number of args only 1 is required
    print("Pas plus d'1 argument mon bro !")
else:
    lettreDepart = ord(firstArg)
    alphabet = ""

    for x in range(lettreDepart,ord('z')+1):
        alphabet += chr(x)
        x++

    print(alphabet)
