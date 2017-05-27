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

# string (file name proposed to be replicated)
PROPOSEDVAL = None

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
NUMACCEPTS = 0

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
    global BALLOTNUM, PROPOSEDVAL, NUMACKS, NUMACCEPTS, ACCEPTNUM, ACCEPTVAL
    try:
        rawData = servsock.recv(1024)
        splitData = rawData.split()
        for ballot in splitData:
            ballotArgs = ballot.split(,)
            if "replicate" in ballot:
                # replicate,fileName
                BALLOTNUM[0] = BALLOTNUM[0] + 1
                PROPOSEDVAL = ballotArgs[1]
                sendPrepare()
            if "prepare" in ballot:
                # prepare,ballot.num, ballot.ID
                prepareNum = ballotArgs[1]
                prepareID = ballotArgs[2]
                incomingBallot = [int(prepareNum), int(prepareID)]
                if firstGreater(incomingBallot, BALLOTNUM):
                    BALLOTNUM[0] = int(prepareNum)
                    BALLOTNUM[1] = prepareID
                    sendAck(incomingBallot)    
            if "ack" in ballot:
                # ack,proposedBal.num, proposedBal.ID,acceptBal.num,acceptBal.ID,acceptVal
                NUMACKS = NUMACKS + 1
                if NUMACKS == 1:
                    incomingBal  = [int(ballotArgs[1]), ballotArgs[2]]
                    incomingAcceptBal = [int(ballotArgs[3]), ballotArgs[4]]
                    incomingVal = ballotArgs[5]                    
                    if incomingVal is None:
                        ACCEPTVAL = PROPOSEDVAL
                    else:
                        #does this work? only 3 nodes so maybe?
                        if firstGreater(ACCEPTNUM, incomingAcceptBal):
                            ACCEPTVAL = PROPOSEDVAL
                        else:
                            ACCEPTVAL = incomingVal
                    leaderAccept()
            if "accept" in ballot:
                #cohortAccept(ballotArgs)
                s

def firstGreater(ballot1, ballot2):
    if ballot1[0] > ballot2[0]:
        return true
    elif ballot1[0] == ballot2[0]:
        if ballot1[1] > ballot2[1]:
            return true
        else:
            return false
    else:
        return false

def sendPrepare():
    for sock in SOCKDICT:
        SOCKDICT[sock].sendall("prepare," + str(BALLOTNUM[0]) + "," + BALLOTNUM[1] + " ")

def sendAck(ballot):
    destination = str(ballot[1])
    SOCKDICT[destination].sendall("ack," + str(ballot[0]) + "," + str(ballot[1]) + "," + str(ACCEPTNUM[0]) + "," + ACCEPTNUM[1] + "," + ACCEPTVAL)

def leaderAccept():
    for sock in SOCKDICT:
        SOCKDICT[sock].sendall("accept," + str(BALLOTNUM[0]) + "," + ACCEPTVAL
                               
def cohortAccept(ballotArgs):

# prep the local log to send as a string to other PRMs
def logToString(aLog):

def stringToLog(aString)
                               
# PRM FUNCTIONS #
def merge(pos1, pos2):
    p1_dict = THELOG[pos1]['words']          #LINE FORMAT: [word] [count]
    p2_dict = THELOG[pos2]['words']
    output = {}
    for word in p1_dict:
        if word not in output:   #NEW INSTANCE OF WORD
            output[word] = p1_dict[word]
        else:                       #WORD ALREADY EXISTS
            output[word] = output[word] + p1_dict[word]
    for word in p2_dict:
        if word not in output:   #NEW INSTANCE OF WORD
            output[word] = p2_dict[word]
        else:                       #WORD ALREADY EXISTS
            output[word] = output[word] + p2_dict[word]
    for index in output:
        print index + ': ' + str(output[index])

def total(pos1, pos2):
    total_count = 0
    p1_dict = THELOG[pos1]['words']         
    p2_dict = THELOG[pos2]['words']
    for word in p1_dict
        total_count = total_count + p1_dict[word]
    for word in p2_dict
        total_count = total_count + p2_dict[word]
    return total_count

def print_log():
    for index in THELOGS:
        print THELOGS[index]['name']


def replicate(filename):
## placeholders for code referencing ##
    THELOGS = {} 
    THELOGS[log_number] = {}       ##log_number = whichever log the file is stored in order
    THELOGS[log_number]['words'] = {}
    THELOGS[log_number]['name'] = filename
    
## end of placeholders ##
    readfile = open(filename, 'r')
    for line in readfile:
        if (len(line.split()) != 2):
            pass
        else:
            word = line.split()[0]      #word
            wc = int(line.split()[1])   #word count
            if word in THELOGS[filename]['words']:     #word already exists in logged dict
                THELOGS[log_number]['words'][word] = THELOGS[filename]['words'][word] + wc 
            else:                                       #word doens't exist, add it
                THELOGS[log_number]['words'][word] = wc
    words = THELOGS[log_number]['words']        
    rep_log = 'makenewlog,' + THELOGS[log_number]['name'] + '/'
    for word in words
        rep_log = rep_log + word + '+' words[word] + '/' 
    #send rep_log to other PRMs to replicate

def stringToLog(logString):
    words = logString.split('/')
    updatedName = False          #check if log has updated name
    THELOGS[log_number] = {}
    THELOGS[log_number]['words'] = {}
    for line in words:
        if not updatedName:
            THELOGS[log_number]['name'] = line
            updatedName = True
        else:
            word = line.split('+')[0]
            wc = int(line.split('+')[1])
            THELOGS[log_number]['words'][word] = wc
    


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
