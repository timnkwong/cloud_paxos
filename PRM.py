#!/usr/bin/env python2
# Dennis Fong, Tim Kwong
# 8234338, 8334492
# 22 May 2017

# ./PRM portNumber fileOfIPs

import sys
import socket

LOCALHOST = '127.0.0.1'
MYPORT = 5004
LISTOFIPS = {}
THELOG = {}

# update the LISTOFIPS dict from config file
def setupIPs():
    with open(sys.argv[1], 'r') as configFile:
        for line in configFile:
            line = line.split()
            LISTOFIPS[line[0]] = 1

def leaderElection():
    s

def checkStream():
    s

def sendPrepare():
    s

def sendAck():
    s

def leaderAccept():
    s

def cohortAccept():
    s

# the main function
setupIPs()
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servsock.bind((LOCALHOST, MYPORT))
servsock.listen(10)
print "Hi"
servsock.close()
