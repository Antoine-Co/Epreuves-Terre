import sys

argument = sys.argv

def isSqrt(entier):
    res = 0
    #Check the only value from 0 to the value but not the float values
    for i in range(entier):
        if (i**2 == entier): #if the pow(2) of a number = value -> the sqrt
            res = i
            break
        else:
            i += 1
            continue
    return res

#Check if the argument is well done and if its a string
if (len(argument) != 2 or argument[1].isalpha()):
    print("Erreur !")
else:
    entier = int(argument[1]) #Get value

    #Check if its positive number
    if (entier < 0):
        print("Erreur !")
    else:
        res = isSqrt(entier)

        #Display the result
        if (res == 0):
            print("Pas de racine carrée entiere !")
        else:
            print(res)
