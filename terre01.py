nameFilePath = __file__
index = -1
lastLetter = nameFilePath[index]

#To find the index of the '/' reversing the name of the path
while lastLetter != '/':
    index -= 1
    lastLetter = nameFilePath[index]

#We keep only the name of the file from the path
nameFile = __file__[index+1:len(__file__)]

print(nameFile)
