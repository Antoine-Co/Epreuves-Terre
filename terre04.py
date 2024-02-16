import sys

argument = sys.argv

#Check if the argument is well done and if its a numeric value
if (len(argument) == 1 or len(argument) > 2 or not argument[1].isnumeric()):
    print("Tu ne me la mettras pas à l’envers.")
else:
    entier = int(argument[1]) #get the numeric value

    #Check if its negative
    if (entier < 0):
        print("Tu ne me la mettras pas à l’envers.")
    else:
        #Check by the modulo if its even or not
        if (entier % 2 == 1):
            print("impair")
        else :
            print("pair")
