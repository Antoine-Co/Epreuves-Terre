import sys

#Get the array of args
arguments = sys.argv

#Function to find the integer square root of a positive int
def getSqrt(inputInt):
    res = 0
    #Check the only value from 0 to the value but not the float values
    for i in range(inputInt):
        if (i**2 == inputInt): #If the number pow(2) = value -> the sqrt
            res = i
            break
        i += 1
    return res

#Check if the argument is well done and if its a string
if (len(arguments) != 2 or arguments[1].isalpha()):
    print("Erreur !")
else:
    inputInt = int(arguments[1]) #Get value

    #Check if its positive number
    if (inputInt < 0):
        print("Erreur !")
    else:
        res = getSqrt(inputInt)

        #Display the result
        if (res == 0):
            print("Pas de racine carrée entiere !")
        else:
            print(res)
