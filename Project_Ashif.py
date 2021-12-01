# -*- coding: utf-8 -*-
"""
@author: ashif
"""

import pandas as pd
from datetime import datetime
from pprint import pprint
import numpy as np                    
from matplotlib import pyplot as plt 
import datetime
import matplotlib.lines as mlines
from datetime import datetime
import math


filenames = ['GHG_final.csv']



neondata = pd.read_csv(filenames[0],
                     delimiter=',', comment='#', header=0,
                 parse_dates=['timestamp'], na_values = [-9999])


neondata = neondata.set_index(['timestamp', 'site'])

#%% Plan of Action
# The plan of action would be to use this NEON measured CO2 data from two study 
#sites initially Flint River, GA (ID: FLNT) and Black Warrior River, AL (ID: BLWA)
#This NEON dataset will be used as in-situ measured data to compare against 
#Theoretically calculated parameters of the same (dissolved CO2 and the evaded CO2
#from the surface water)
# The USGS datasets primarily aimed to use are USGS 02344500 and USGS 02465000
# of the same rivers respectively. The discharge dataset will be used to identify 
# the response of storm events on the dissolved CO2 and CO2 evasion from the surface
# water. 
# I hope to see some temporal and spatial variability in CO2 evasion from these 
# surface water and might include additional sites to see if any pronounced difference
# is noticable across sites and would try to identify the driver causing the difference.

# As the progress is at very preliminary stage, I could not generate any plot at this 
# moment. I apologize for that.