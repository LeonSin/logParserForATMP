# -*- coding: utf-8 -*-
import re

m1 = re.search(r'Unpack field\[000:\s+\]=\[len=\d+\]', '[INFO] 0926 21:49:27.170[FEP][fIhxlhhywpYC] POS_FEP:52||Unpack field[000:                    ]=[len=4]<0200>')
if m1:
    print 'find'