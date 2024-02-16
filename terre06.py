import sys

argument = sys.argv

#Check if the argument is well done and if its a number
if (len(argument) > 2 or argument[1].isnumeric()):
    print("Erreur !")
else:
    chaine = argument[1] #Get value

    res = ""
    while chaine != "":
        res += chaine[-1]     #Taking the last character
        chaine = chaine[0:-1] #Substring without the last char

    print(res)
