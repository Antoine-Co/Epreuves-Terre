import sys

argument = sys.argv

#Check if the argument is well done and if its a number
if (len(argument) != 2 or argument[1].isnumeric()):
    print("Erreur !")
else:
    chaine = argument[1] #Get value

    cpt = 0 #Counter
    while chaine != "":
        chaine = chaine[0:-1]
        cpt += 1              #Increment while deleting a char of the string

    print(cpt)
