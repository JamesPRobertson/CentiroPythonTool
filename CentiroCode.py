class Customer:
  def makeString(self):
    print(self.orderNo + " " + self.name + "   " + self.status)
 
inFile = open("inFile.txt","r+")
outFile  = open("outPutFile.txt", "w+")
 
customerList = []

for line in inFile:
  tempString = line.split(";")
 
  foo = Customer()
  foo.orderNo = tempString[0]
  foo.name = tempString[1]
  foo.status = tempString[11]
 
  customerList.append(foo)
 
for foo in customerList:
  foo.makeString()
 