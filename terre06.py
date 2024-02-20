import sys

#Get the array of args
arguments = sys.argv

#Check if the argument is well done and if its a number
if (len(arguments) > 2 or arguments[1].isnumeric()):
    print("Erreur l'argument attendu est une chaîne de caractères !")
    exit()

chaine = arguments[1] #Get value

res = ""
while chaine != "":
    res += chaine[-1]     #Taking the last character
    chaine = chaine[0:-1] #Substring without the last char

#Display the result of the reversed string
print(res)
