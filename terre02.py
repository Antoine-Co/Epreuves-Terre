import sys

arguments = sys.argv

#For each args passed to the script avoiding the name of the script
for i in range(1,len(arguments)):
    print(arguments[i])
