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
BALLOTNUM = 0

# string to string
# siteID to IP
LISTOFIPS = {}

# the nested 3d dictionary
THELOG = {}

# string to socket
# IP to socket
SOCKDICT = {}

# int to int
# BALLOTUM to MYID
BALLOTDICT = {}

ISLEADER = 0

# update the LISTOFIPS dict from config file and MYIP
def setupConfig():
    with open(sys.argv[2], 'r') as configFile:
        for line in configFile:
            line = line.split()
            if line[0] == MYID:
                MYIP = line[0]
            else:
                LISTOFIPS[line[0]] = line[1]

# connect to all other PRMs
def setupPorts():
    for siteID in LISTOFIPS
        addr = (LISTOFIPS[siteID], 5004)
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
                #sendPrepare()
                #initiate the paxos algorithm
            if "prepare" in ballot:
                #sendAck(ballotArgs)    
            if "ack" in ballot:
                #leaderAccept(ballotArgs)
            if "accept" in ballot:
                #cohortAccept(ballotArgs)

def sendPrepare():
    global ISLEADER, BALLOTNUM
    ISLEADER = 1
    BALLOTNUM = BALLOTNUM + 1
    BALLOTDICT[BALLOTNUM] = MYID
    for sock in SOCKDICT:
        SOCKDICT[sock].sendall("prepare," + str(BALLOTNUM) + "," + str(MYID) + " "

def sendAck(ballotArgs):

def leaderAccept(ballotArgs):

def cohortAccept(ballotArgs):

# the main function
setupConfig()
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servsock.bind((LOCALHOST, PORT))
servsock.listen(10)

time.sleep(5)
setupPorts()

servsock.close()
for sock in SOCKDICT:
    SOCKDICT[sock].close()
