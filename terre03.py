import sys

#Get the array of args
arguments = sys.argv

#Check the arguments and if its a letter
if (len(arguments) != 2 or not arguments[1].isalpha() or not len(arguments[1]) == 1):
    print("Dsl il faut une seule lettre en argument.")
    exit()

lettreDepart = ord(arguments[1])  #Get the position of the letter in the ascii table
alphabet = ""

#Loop from position of the letter to the position of the letter "z"
for x in range(lettreDepart,ord('z')+1):
    alphabet += chr(x)
    x += 1

#Display the alphabet from the letter given
print(alphabet)
