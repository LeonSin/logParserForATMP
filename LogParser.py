# -*- coding: utf-8 -*-
import os
import re


def parseTxSerialNo(line):
    #'^([?P<level>\w+]) (?P<date>\d+)
    m = re.search(r'channelID:\[(?P<channelID>\w+)\] txCode:\[(?P<txCode>\w+)\]', line)
    if m:
        print m.group("channelID") + " " + m.group("txCode")



logDir = 'C:\Users\lenovo\Desktop\logFile\\'

logFileList = os.listdir(logDir)

for logFile in logFileList:
    logQualifiedName = logDir + logFile
    print logQualifiedName
    with open(logQualifiedName, 'rb') as f:
        for line in f.readlines():
            parseTxSerialNo(line)

