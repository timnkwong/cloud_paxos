#!/usr/bin/env python2
# Dennis Fong, Tim Kwong
# 8234338, 8334492
# 22 May 2017

# ./PRM siteID fileOfIPs

import sys
import socket

MYIP = 0
MYID = sys.argv[1]
PORT = 5004
LISTOFIPS = {}
THELOG = {}
SOCKDICT = {}

# update the LISTOFIPS dict from config file and MYIP
def setup():
    with open(sys.argv[2], 'r') as configFile:
        for line in configFile:
            line = line.split()
            if line[0] == MYID:
                MYIP = line[0]
            else:
                LISTOFIPS[line[0]] = line[1]

def setupPorts():
    for sock in LISTOFIPS
        
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
                
            if "ack" in ballot:

            if "accept" in ballot:

def sendPrepare():
    s

def sendAck():
    s

def leaderAccept():
    s

def cohortAccept():
    s

# the main function
setup()
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servsock.bind((LOCALHOST, PORT))
servsock.listen(10)

time.sleep(5)
setupPorts()

servsock.close()
