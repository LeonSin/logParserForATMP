# -*- coding: utf-8 -*-
import os
import re


def parse_tx_code(line):
    #'^([?P<level>\w+]) (?P<date>\d+)
    m = re.search(r'channelID:\[(?P<channelID>\w+)\] txCode:\[(?P<txCode>\w+)\]', line)
    if m:
        print m.group("channelID") + " " + m.group("txCode")


def parse_packet_message_field(line):
    for index in range(128):
        m = re.search(r'Unpack field\[' + str(index).zfill(3) + ':\s+\]=\[len=\d+\]<(?P<message>\w+)>', line)
        if m:
            print "field[" + str(index).zfill(3) + "]=" + m.group("message")


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
                parse_tx_code(line)
                parse_packet_message_field(line)
                parse_tx_serial_no(line)

