# -*- coding: utf-8 -*-
import re

c = re.compile(r'channelID')
m = c.match(r'channelID', '[DEBUG ] 0926 21:49:21.865[FEP][fIdLegKIMsFB] POS_FEP:48||channelID:[POS_VM] txCode:[P_ADJ0]')

