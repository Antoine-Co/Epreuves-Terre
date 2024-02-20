import sys

#Get the array of args
arguments = sys.argv
intTab = []

#Checking the arguments and adding all of them in a list if its numeric
for i in range(1,len(arguments)):
    if(not arguments[i].isnumeric()):
        print("Erreur les arguments attendus doivent être une liste d'entiers.")
        exit()
    else:
        intTab.append(int(arguments[i]))

#Necessary to have a list of at least 2 int
if (len(intTab) < 2):
    print("Il faut un liste d'entiers avec minimum 2 entiers !")
    exit()

#Boolean function return True if a list is sorted
def isSorted(intTab):
    if(intTab[0] <= intTab[1]):
        if (len(intTab) > 2):                          #Lenght > 2 because we can only compare 2 elts
            return tableauTri(intTab[1:len(intTab)])   #Recursivity with the array without the fisrt elt
        elif (len(intTab) == 2):
            return True
        else:
            return False
    else:
        return False


if(isSorted(intTab) == True):
    print("Trié")
else:
    print("Non trié")
