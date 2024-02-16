import sys

argument = sys.argv

#Check if the argument is well done and if its a numeric value
if (len(argument) <= 2 or len(argument) > 3 or not argument[1].isnumeric()
    or not argument[2].isnumeric() ):
    print("Tu ne me la mettras pas à l’envers.")
else:
    entier1 = int(argument[1]) #get the numeric values
    entier2 = int(argument[2])

    #Check for the division by 0 or divisor > dividend
    if (entier2 == 0 or entier2 > entier1):
        print("Erreur.")
    else:
        print("Résultat: ", entier1//entier2) #int division
        print("Reste: ", entier1%entier2) #modulo for the remainder
