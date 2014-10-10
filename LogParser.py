# -*- coding: utf-8 -*-
import os
import re

def parseTxSerialNo(line):
    #'^([?P<level>\w+]) (?P<date>\d+)
    m = re.match(r"channelID:[?P(<channelID>\w+_\w+)]", line)
    if m:
        print '1'\
            #m.group("channelID")

logDir = 'C:\Users\lenovo\Desktop\logFile\\'

logFileList = os.listdir(logDir)

for logFile in logFileList:
    print logDir + logFile
    with open(logDir + logFile, 'rb') as f:
        for line in f.readlines():
            parseTxSerialNo(line)

