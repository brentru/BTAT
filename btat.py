#!/usr/bin/env Python

"""
BTAT

    btat [-h, --help] [--version] [-d, --debug]

DESCRIPTION

    Automated penetration testing tool for enumerating
    bluetooth devices, vendor ID, and distributing payloads.

AUTHOR(s)

    @brentru, @daustin1, @epires3

LICENSE

    2017, MIT License
VERSION

    $Id$
"""
import csv
import subprocess
from optparse import OptionParser

vendorList = []
btaddrList = []
dbgMode = False

def csvParser(dbgMode):
    print dbgMode
    if(dbgMode == True):
        print 'DBG: opening csv..'
    with open('bt_database.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            vendorList.append(row[0])
            btaddrList.append(row[1])
    print 'Bluetooth Addresses Scraped: \n', btaddrList
    print '\nVendors Enumerated: \n', vendorList

def payloadDropper(btaddrList, vendorList):
    for i in range(btaddrList):
        subprocess.call("payload.py TARGET=", btaddrlist[i])


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
        csvParser(dbgMode)

if __name__ == '__main__':
    main()
