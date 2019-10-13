inFile = open("inFile.txt","r+")
outFile  = open("outPutFile.txt", "w+")
 
customerList = []

for line in inFile:
    tempString = line.split(";")
    nameSplit = tempString[1].split(" ")

    foo = dict(orderNo = tempString[0], fullName = tempString[1],
    lastName = nameSplit[1], status = tempString[11])

    customerList.append(foo)

printList = sorted(customerList, key = lambda i: i['lastName'])   

for foo in printList:
    print("{f[orderNo]} {f[fullName]:25} {f[status]}".format(f = foo))
