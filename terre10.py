import sys

#Get the array of args
arguments = sys.argv

#Function that return an array of all divisors of an int
def getDivisors(inputInt):
    #Each number have himself and 1 as divisor
    divisors = [1, inputInt]

    #From 2 to the int - 1 because we already have it
    for i in range(2,inputInt):
        if (inputInt%i == 0):    #Modulo to find ones = 0
            divisors.append(i)
        i += 1

    return divisors

#Check if the argument is well done
if (len(arguments) != 2 or not arguments[1].isnumeric()):
    print("Erreur l'argument attendu est un entier !")
    exit()

inputInt = int(arguments[1]) #Get value and convert to int for comparison

# Negatives and 0 , 1 are not prime
if (inputInt <= 1):
    print("Erreur l'entier en argument doit être > 1!")
else:
    #If the list of divisors is == 2 himself and 1 so it's prime
    if (len(getDivisors(inputInt)) == 2):
        print("Oui, " + str(inputInt) + " est un nombre entier !")
    else :
        print("Non, " + str(inputInt) + " n'est pas un nombre entier !")
