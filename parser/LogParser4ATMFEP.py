# -*- coding: utf-8 -*-
import os
import re

txList = []
txListLogLine = {}


def search_transaction(line):
    global txList
    match = re.search(r'Put request data into sendBlockingQueue txSerialNo=(?P<txSerialNo>\w+)', line)
    if match:
        txList.append(match.group("txSerialNo"))


def parse_tx_code(line):
    #'^([?P<level>\w+]) (?P<date>\d+)
    m = re.search(r'outTxCdoe=\[(?P<outTxCdoe>\w+)\] innerTxCode=\[(?P<innerTxCode>\w+)\]', line)
    if m:
        print m.group("outTxCdoe") + " " + m.group("innerTxCode")


def parse_message_fep2txe(line):
    match = re.search(r'Put response data into MQ:FEP2TXE detail:\[(?P<message>\w+)\]', line)
    if match:
        print match.group("message")


def parse_tx_serial_no(line):
    match = re.search(r'The current transaction serial number:(?P<txSerialNo>\w+)', line)
    if match:
        print match.group("txSerialNo")


if __name__ == '__main__':
    logDir = 'C:\Users\lenovo\Desktop\logFile\\'

    logFileList = os.listdir(logDir)

    for logFile in logFileList:
        logQualifiedName = logDir + logFile
        print logQualifiedName
        with open(logQualifiedName, 'rb') as f:
            for line in f.readlines():
                search_transaction(line)

    print txList
