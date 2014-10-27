# -*- coding: utf-8 -*-
import os
import re


def parseTxSerialNo(line):
    #'^([?P<level>\w+]) (?P<date>\d+)
    m = re.search(r'channelID:\[(?P<channelID>\w+)\] txCode:\[(?P<txCode>\w+)\]', line)
    if m:
        print m.group("channelID") + " " + m.group("txCode")


def parsePacketMessageField(line):
    for index in range(128):
        m = re.search(r'Unpack field\[' + str(index).zfill(3) + ':\s+\]=\[len=\d+\]<(?P<message>\w+)>', line)
        if m:
            print "field[" + str(index).zfill(3) + "]=" + m.group("message")

logDir = 'C:\Users\lenovo\Desktop\logFile\\'

logFileList = os.listdir(logDir)

for logFile in logFileList:
    logQualifiedName = logDir + logFile
    print logQualifiedName
    with open(logQualifiedName, 'rb') as f:
        for line in f.readlines():
            parseTxSerialNo(line)
            parsePacketMessageField(line)

