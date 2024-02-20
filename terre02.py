import sys

#Get the array of args
arguments = sys.argv

#Loop for each args passed to the script (begin at 1 : don't want the name of the sript)
for i in range(1,len(arguments)):
    print(arguments[i])
