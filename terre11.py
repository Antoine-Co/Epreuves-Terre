import sys

argument = sys.argv

#Check if the argument is ok
if (len(argument) != 2):
    print("Erreur donnez une heure format 24h !")
else:
    heureFormat24 = argument[1] #Get string value

    #Convert to int
    heures = int(heureFormat24[0:2]) #conversion to int for comparaison
    minutes = heureFormat24[3:len(heureFormat24)]

    indicateur=""

    #Check if hours > 12 for indicator AM or PM
    if (heures >= 12):
        indicateur = "PM"
        if (heures != 12):
            heures = heures%12 #If its > 12 making modulo for the 12 format
    elif (heures < 12):
        indicateur = "AM"
        if (heures == 0):      #If its midnight set to 12
            heures = 12

    #To set the hour with 2 digit ex: 1 -> 01
    if (heures < 10):
        heures = "0" + str(heures)

    #Display hour in 12 hour format
    print(heures, ":", minutes, indicateur)
