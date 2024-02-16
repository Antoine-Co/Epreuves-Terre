import sys

argument = sys.argv

#Check if the argument is well done and if its a string
if (len(argument) != 3 or argument[1].isalpha() or argument[2].isalpha()):
    print("Erreur !")
else:
    entier1 = int(argument[1]) #Get values
    entier2 = int(argument[2])

    #Check if the exponent is < 0
    if(entier2 < 0):
        print("Erreur !")
    else:
        print(entier1**entier2)
