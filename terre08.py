import sys

#Get the array of args
arguments = sys.argv

#Check if the argument is well done and if its a string
if (len(arguments) != 3 or arguments[1].isalpha() or arguments[2].isalpha()):
    print("Erreur il faut 2 arguments et 2 entiers !")
else:
    int1 = int(arguments[1]) #Get values
    int2 = int(arguments[2])

    #Check if the exponent is < 0
    if(int2 < 0):
        print("Erreur l'exposant est négatif !")
    else:
        print(int1**int2)
