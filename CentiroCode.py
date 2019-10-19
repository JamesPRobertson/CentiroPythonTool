#A simple script for formatting Centiro reports

#Create a list of all files in the current directory
import glob

dirList = glob.glob('*.csv')

#Open the first one if we found anything
if len(dirList) == 0:
    raise RuntimeError("No matching files found: *.csv")
else:
    inFile = open(dirList[0],"r+")

outFile  = open("outputFile.txt", "w+")

#Create two empty lists to hold dictionaries for each line parsed
standardList = []
irregularList = []

for line in inFile:
    #Each line in the file is formatted in a specific way
    #However, the first line is reserved for the header and always starts with "Order"
    if(line[0] == "O"):
        continue

    tempString = line.split(";")
    nameSplit = tempString[1].split(" ")

    #Thankfully Python has a built in key based structure for easy sorting
    #fullName is used for output and it's formatting, while lastName is used for sorting the lists later
    tempDict = dict(orderNo = tempString[0], fullName = tempString[1],
    lastName = nameSplit[1], status = tempString[11])

    #Checking the dictionary for an order status that is irregular
    if tempDict['status'] == "SP_CONTACTED sent to iSell" or tempDict['status'] == "Received at Hub":
        standardList.append(tempDict)
    else:
        irregularList.append(tempDict)

#Reassign the lists to a sorted version of themselves using a lambda function
standardList = sorted(standardList, key = lambda i: i['lastName'])
irregularList = sorted(irregularList, key = lambda i: i['lastName'])

#All that is left is to write to the output file
outFile.write("*********************************************************************\n")

for entry in standardList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")

outFile.write("\n*********************************************************************")
outFile.write("\nThese orders need attention:\n\n")

for entry in irregularList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")
