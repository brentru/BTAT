#!/usr/bin/env Python

"""
BTAT

    btat [-h, --help] [--version] [-d, --debug]

DESCRIPTION

    Companion Tool for Blue Hydra to scrape log database for
    BTADDR, device name, vendor ID and perform payload distribution and logging.

AUTHOR(s)

    Developed for ECE488/548 Class at UMass Dartmouth by:
    @brentru, @daustin1, and  @epires3

LICENSE

    2017, MIT License

VERSION

    $Id$

"""
import csv
from optparse import OptionParser
import subprocess

# lists for handset data
nameList = []
vendorList = []
btaddrList = []
dbgMode = False

def csvParser(dbgMode=False):
    #print dbgMode
    if(dbgMode == True):
        print 'DBG: opening csv..'
    with open('bt_database.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            btaddrList.append(row[2])
            nameList.append(row[3])
            vendorList.append(row[4])

    # array formatting needs to be stripped
    # and put back into the array before printing
    print 'Device Names: \n', nameList
    print 'Bluetooth Addresses Scraped: \n', btaddrList
    print 'Vendors Enumerated: \n', vendorList

def payloadDropper(btaddrList, vendorList):
    # placeholder call, replace with loop for btaddresses
    subprocess.call("payload.py TARGET=80:D5:05:1E:41:54")

def main():
    parser = OptionParser(usage="usage %prog [options]",
                            version="%prog 1.0")
    parser.add_option("-d", "--debug",
                      action = "store_true",
                      dest= "debug",
                      default = False,
                      help= "runs in a verbose debug mode")
    (options, args) = parser.parse_args()
    if(options.debug == True):
        csvParser(dbgMode = True)
    else:
        csvParser()

if __name__ == '__main__':
    main()
