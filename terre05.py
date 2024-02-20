import sys

#Get the array of args
arguments = sys.argv

#Check if the argument is well done and if its a numeric value
if (len(arguments) != 3 or not arguments[1].isnumeric() or not arguments[2].isnumeric()):
    print("Tu ne me la mettras pas à l’envers. Il faut 2 arguments entiers.")
    exit()

int1 = int(arguments[1]) #Convert string to numeric values
int2 = int(arguments[2])

#Check for the division by 0 or divisor > dividend
if (int2 == 0 or int2 > int1):
    print("Erreur. Division par 0 ! Ou diviseur > dividende.")
else:
    print("Résultat: ", int1//int2) #Int division
    print("Reste: ", int1%int2) #Modulo for the remainder
