#!/usr/bin/env python2
# Dennis Fong, Tim Kwong
# 8234338, 8334492
# 22 May 2017

# ./PRM siteID fileOfIPs

import sys
import socket
import time

MYIP = 0
MYID = sys.argv[1]
PORT = 5004

# int, string
# ballotNumber, aSiteID
BALLOTNUM = [0, 0]
ACCEPTNUM = [0, 0]

# string (file name to be replicated)
ACCEPTVAL = None

# dict for phase 2 to check if already have received accept
ACCEPTDICT = {}

# dict for phase 2 to check for all vals  = null
ACKDICT = {}

# string to string
# siteID to IP
IPDICT = {}

# the nested 3d dictionary
THELOG = {}

# string to socket
# IP to socket
SOCKDICT = {}

NUMACKS = 0

# update the LISTOFIPS dict from config file and MYIP
def setupConfig():
    with open(sys.argv[2], 'r') as configFile:
        for line in configFile:
            line = line.split()
            if MYID in line[0]:
                MYIP = line[0]
            else:
                IPDICT[line[0]] = line[1]

# connect to all other PRMs
def setupPorts():
    for siteID in IPDICT
        addr = (IPDICT[siteID], 5004)
        SOCKDICT[siteID] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCKDICT[siteID].connect(addr)

#  messages sent with spaces after each other, ballots separated by commas
def checkStream():
    try:
        rawData = servsock.recv(1024)
        splitData = rawData.split()
        for ballot in splitData:
            ballotArgs = ballot.split(,)
            if "replicate" in ballot:
                BALLOTNUM[0] = BALLOTNUM[0] + 1
                sendPrepare()
            if "prepare" in ballot:
                prepareNum = ballotArgs[1]
                prepareVal = ballotArgs[2]
                incomingBallot = [int(prepareNum), int(prepareVal)]
                if firstGreater(BALLOTNUM, incomingBallot)):
                    BALLOTNUM[0] = int(prepareNum)
                    BALLOTNUM[1] = prepareVal
                    sendAck(incomingBallot)    
            if "ack" in ballot:
                NUMACKS = NUMACKS + 1
                tempBal  = [int(ballotArgs[1]), ballotArgs[2]]
                tempAcceptBal = [int(ballotArgs[3]), ballotArgs[4]]
                tempVal = ballotArgs[5]
                if NUMACKS == 1:
                    
                #if received 2 ack
                    #continue?
                #leaderAccept(ballotArgs)
            if "accept" in ballot:
                #cohortAccept(ballotArgs)

def firstGreater(ballot1, ballot2):
    if ballot1[0] > ballot2[0]:
        return true
    elif ballot1[0] == ballot2[0]:
        if ballot1[1] > ballot2[1]:
            return true
        else
            return false
    else
        return false

def sendPrepare():
    for sock in SOCKDICT:
        SOCKDICT[sock].sendall("prepare," + str(BALLOTNUM) + "," + str(MYID) + " "

def sendAck(ballot):
    destination = str(ballot[1])
    SOCKDICT[destination].sendall("ack," + str(ballot[0]) + "," + str(ballot[1]) + "," + str(ACCEPTNUM[0]) + "," + ACCEPTNUM[1] + "," + ACCEPTVAL)
        
def leaderAccept(ballotArgs):

def cohortAccept(ballotArgs):

# prep the local log to send as a string to other PRMs
def logToString(aLog):

def stringToLog(aString)

# store the file_reduced.txt into our local log
def parseReduced(reducedFileName):

# the main function
setupConfig()
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servsock.bind((LOCALHOST, PORT))
servsock.listen(10)

time.sleep(5)
setupPorts()

# keep while loop running to checkStream()

servsock.close()
for sock in SOCKDICT:
    SOCKDICT[sock].close()
