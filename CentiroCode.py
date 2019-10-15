import glob

dirList = glob.glob('*.csv')

inFile = open(dirList[0],"r+")
outFile  = open("outputFile.txt", "w+")

customerList = []
standardList = []
irregularList = []

for line in inFile:
    tempString = line.split(";")
    nameSplit = tempString[1].split(" ")

    foo = dict(orderNo = tempString[0], fullName = tempString[1],
    lastName = nameSplit[1], status = tempString[11])

    customerList.append(foo)

for entry in customerList:
    if entry['status'] != "SP_CONTACTED sent to iSell" and entry['status'] != "Received at Hub":
        irregularList.append(entry)
    else:
        standardList.append(entry)

printList = sorted(customerList, key = lambda i: i['lastName']) 

outFile.write("*********************************************************************\n")

for entry in standardList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")

outFile.write("\n*********************************************************************")
outFile.write("\nThese orders need attention:\n")

for entry in irregularList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")
