import sys

#Get the array of args
arguments = sys.argv
hourFormat12 = ""

#Checking the lenght of the input first time
if(len(arguments) != 2 or len(arguments[1]) != 7) :
    print("Erreur votre heure en argument doit être en format 12h (ex = 11:45PM)")
    exit()

hourFormat12 = arguments[1] #Get string value

#Convert argument into string variables
indicator = hourFormat12[-2:len(hourFormat12)] #Take the last 2 chars for the indicator
minutes = hourFormat12[3:-2]
hours = hourFormat12[0:2]

#Checking the input correctly formed second time
if(not indicator.isalpha() or not hours.isnumeric() or not minutes.isnumeric()
    or int(hours) > 12 or int(minutes) > 59 or (indicator != "AM" and indicator != "PM")) :
    print("Erreur votre heure en argument doit être en format 12h (ex = 11:45PM)")
    exit()

#Convert hour to int for comparison
hours = int(hours)

#Depend on the indicator of the AM/PM -> hours change
if(indicator == "AM"):
    if(hours == 12):
        hours = 0        #For midnight
elif (indicator == "PM"):
    if(hours != 12):
        hours += 12      #Adding 12 to have the 24h format

#To set the hour with 2 digit ex: 1 -> 01
if(hours < 10):
    hours = "0" + str(hours)
else:
    hours = str(hours) #Convert hours to string  for printing

#Diplay hour in 24h format
print(hours + ":" + minutes)
