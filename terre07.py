import sys

#Get the array of args
arguments = sys.argv

#Check if the argument is well done and if its a number
if (len(arguments) != 2 or arguments[1].isnumeric()):
    print("Erreur l'argument doit être une seule chaîne de caractères !")
    exit()

words = arguments[1]      #Get value

cpt = 0 #Counter
while words != "":
    words = words[0:-1]
    cpt += 1              #Increment counter while deleting a char of the string

#Diplay the lenght of a string
print(cpt)
