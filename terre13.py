import sys

#Get the array of args
arguments = sys.argv

#Checking the lenght of the input first time
if(len(arguments) != 4 or not arguments[1].isnumeric() or not arguments[2].isnumeric()
    or not arguments[3].isnumeric()):
    print("Erreur les 3 arguments attendus doivent être des entiers.")
    exit()

int1 = int(arguments[1]) #Convert string to int
int2 = int(arguments[2])
int3 = int(arguments[3])

#Init array
tab = []

#Checking for the all values equals
if (int1 == int2 == int3):
    print("Erreur tous les entiers sont égaux!")
#Making first the comparison between int1 and int2
elif (int1 > int2):
    if (int1 > int3): #Compare to the int3 and completing all cases
        if (int3 > int2):
            tab.append(int2)
            tab.append(int3)
            tab.append(int1)
        else:
            tab.append(int3)
            tab.append(int2)
            tab.append(int1)
    else:
        tab.append(int2)
        tab.append(int1)
        tab.append(int3)
else: #We already know that int1 < int2 just have to complete all cases
    if (int1 < int3):
        if (int2 < int3):
            tab.append(int1)
            tab.append(int2)
            tab.append(int3)
        else:
            tab.append(int1)
            tab.append(int3)
            tab.append(int2)
    else:
        if (int1 > int3):
            tab.append(int3)
            tab.append(int1)
            tab.append(int2)
        else:
            ab.append(int1)
            tab.append(int3)
            tab.append(int2)

#In the tab the second value is the one in the middle
print(tab[1])
