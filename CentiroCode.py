import glob

dirList = glob.glob('*.csv')

if len(dirList) == 0:
    raise RuntimeError("No matching files found: *.csv")

inFile = open(dirList[0],"r+")
outFile  = open("outputFile.txt", "w+")

standardList = []
irregularList = []

for line in inFile:
    tempString = line.split(";")
    nameSplit = tempString[1].split(" ")

    tempDict = dict(orderNo = tempString[0], fullName = tempString[1],
    lastName = nameSplit[1], status = tempString[11])

    if tempDict['status'] == "SP_CONTACTED sent to iSell" or tempDict['status'] == "Received at Hub":
        standardList.append(tempDict)
    else:
        irregularList.append(tempDict)

standardList = sorted(standardList, key = lambda i: i['lastName'])
irregularList = sorted(irregularList, key = lambda i: i['lastName'])

outFile.write("*********************************************************************\n")

for entry in standardList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")

outFile.write("\n*********************************************************************")
outFile.write("\nThese orders need attention:\n\n")

for entry in irregularList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")
