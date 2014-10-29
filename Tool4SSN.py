# -*- coding: utf-8 -*-

import os
import re

term_serialNo_list = []
ssn_dic = {}
fova_serialNo_dic = {}
term_serialno_dic = {}

def term_serialno_parse():
    lines = find_XML_message_by_keyword('Receive data from the MQ')
    for line in lines:
        match = re.search(r'Receive data from the MQ=\[<.*><Transaction_SerialNo>(?P<Transaction_SerialNo>\w+)</Transaction_SerialNo><.*><SerialNo>(?P<SerialNo>\w+)</SerialNo><.*>', line)
        if match:
            term_serialno_dic[match.group("SerialNo")] = match.group("Transaction_SerialNo")
            term_serialNo_list.append(match.group("SerialNo"))
        else:
            term_serialno_dic[match.group("SerialNo")] = ""
            term_serialNo_list.append(match.group("SerialNo"))

def ssn_parse():
    lines = find_XML_message_by_keyword('Put the response data')
    for line in lines:
        match = re.search(r'Put the response data\[<.*><TLV_Host>(?P<TLV_Host>\w+)</TLV_Host><.*><SysTraceNo>(?P<SysTraceNo>\w+)</SysTraceNo><.*><SerialNo>(?P<SerialNo>\w+)</SerialNo><.*>', line)
        if match:
            fova_serialNo_dic[match.group("SerialNo")] = match.group("SysTraceNo")
            ssn_match = re.search(r'2F02\d{2}(?P<date>\d{12})(?P<ssn>\d{12})', match.group("TLV_Host"))
            if ssn_match:
                ssn_dic[match.group("SerialNo")] = ssn_match.group("ssn")[1::2]
            else:
                ssn_dic[match.group("SerialNo")] = ""
        else:
            fova_serialNo_dic[match.group("SerialNo")] = ""


def find_XML_message_by_keyword(keyword):
    file_line_list = []
    logFileList = os.listdir('.')
    for logFile in logFileList:
        if logFile.endswith('log'):
            with open(logFile, 'rb') as log:
                for line in log.readlines():
                    if keyword in line:
                        file_line_list.append(line)
    return file_line_list


if __name__ == '__main__':
    #term_serialno_parse()
    #ssn_parse()
    #with open('term_serialNo.txt', 'ab+') as f:
    #    for line in f.readlines():
    #        term_serialNo = line.strip()
    #        if re.match('\d+', term_serialNo):
    #            term_serialNo_list.append(term_serialNo)
    #    print term_serialNo_list
    #    f.seek(0)
    #    f.truncate(0)
    #    for serialNo in term_serialNo_list:
    #        f.write(serialNo + "\n")
    #    f.write('\n\n--------result--------')
    term_serialno_parse()
    ssn_parse()
    with open('result.txt', 'w+') as f:
        f.write('--------result--------\n')
        for term_serialno in term_serialNo_list:
            print term_serialno
            f.write('ATMP_serialNo:' + term_serialno + "  ")
            f.write('term serialNo:' + term_serialno_dic[term_serialno] + "  ")
            f.write('fova_serialNo:' + fova_serialNo_dic[term_serialno] + "  ")
            f.write('SSN:' + ssn_dic[term_serialno] + "  \n")
