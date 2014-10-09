# -*- coding: utf-8 -*-

with open('C:\Users\lenovo\Desktop\logFile\POS_FEP_2014-09-26.log.1', 'rb') as f:
    serialNo = 'fIcjMlq1yN9e'
    for line in f.readlines():
        if serialNo in line:
            print line

