inFile = open("inFile.txt","r+")
outFile  = open("outputFile.txt", "w+")

customerList = []

for line in inFile:
    tempString = line.split(";")
    nameSplit = tempString[1].split(" ")

    foo = dict(orderNo = tempString[0], fullName = tempString[1],
    lastName = nameSplit[1], status = tempString[11])

    customerList.append(foo)

printList = sorted(customerList, key = lambda i: i['lastName']) 

for entry in printList:
    outFile.write("[ ] {f[orderNo]} {f[fullName]:28.26} {f[status]:.26}".format(f = entry) + "\n")
