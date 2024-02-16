import sys

argument = sys.argv

def isPrime(entier):
    #Each number have himself and 1 as divisor
    divisors = [1, entier]

    #From 2 to the int - 1 because we already have it
    for i in range(2,entier):
        if (entier%i == 0):    #Modulo to find ones = 0
            divisors.append(i)
        i += 1

    return divisors

#Check if the argument is well done and if its a string
if (len(argument) != 2 or argument[1].isalpha()):
    print("Erreur !")
else:
    entier = int(argument[1]) #Get value

    # Negatives and 0 , 1 are not prime
    if (entier <= 1):
        print("Erreur !")
    else:
        #if the list of divisors is == 2 himself and 1 so it's prime
        if (len(isPrime(entier)) == 2):
            print("Oui, ", entier, " est un nombre entier !")
        else :
            print("Non, ", entier, " n'est pas un nombre entier !")
