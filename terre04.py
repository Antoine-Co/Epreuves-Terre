import sys

#Get the array of args
arguments = sys.argv

#Check if the argument is well done and if its a numeric value
if (len(arguments) != 2 or not arguments[1].isnumeric()):
    print("Tu ne me la mettras pas à l’envers. L'argument attendu est un entier.")
    exit()

int1 = int(arguments[1]) #Convert arg to int

#Check by the modulo 2 if its even or not
if (int1 % 2 == 1):
    print("Impair")
else :
    print("Pair")
