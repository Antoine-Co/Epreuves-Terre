import sys

#Get the array of args
arguments = sys.argv
hourFormat24 = ""

#Checking the input first time
if(len(arguments) != 2 or len(arguments[1]) != 5) :
    print("Erreur votre heure en argument doit être en format 24h (ex = 23:40)")
    exit()

hourFormat24 = arguments[1] #Get string value

#Getting values
hours = hourFormat24[0:2]
minutes = hourFormat24[3:len(hourFormat24)]

#Checking the input arguments second time
if (not hours.isnumeric() or not minutes.isnumeric() or int(hours) > 23 or int(minutes) > 59):
    print("Erreur votre heure en argument doit être en format 24h (ex = 23:40)")
    exit()

#Conversion to int for comparaison and init indicator
hours = int(hours)
indicator = ""

#Check if hours > 12 for indicator AM or PM
if (hours >= 12):
    indicator = "PM"
    if (hours != 12):
        hours = hours%12 #If its > 12 making modulo for the 12 format
elif (hours < 12):
    indicator = "AM"
    if (hours == 0):     #If its midnight 00 set hour to 12
        hours = 12

#To set the hour with 2 digit ex: 1 -> 01
if (hours < 10):
    hours = "0" + str(hours)
else:
    hours = str(hours)   #Convert hours to string  for printing

#Display hour in 12h format
print(hours + ":" + minutes + indicator)
