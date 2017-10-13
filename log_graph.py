"""
Title: Reading a LogFile with Data Recorded and Prodicing a Graph
Created on Thu Oct 10 14:49:20 2017
Modified:
@author: Kevin Machado Gamboa
Ref: Raspberry pi Cookbook 1 for python programmers. chapter 7 Pag. 210
"""
# !/usr/bin/env python3
# log_graph.py
# -----------------------------------------------------------------------------
## Importing modules and creating variables

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

filename = "data.log"
OFFSET=2
with open(filename) as f:
    header = f.readline().split('\t')

data = np.genfromtxt(filename, delimiter='\t', skip_header=1,
                     names=['sample', 'date', 'DATA0',
                            'DATA1', 'DATA2', 'DATA3'])
fig = plt.figure(1)
ax1 = fig.add_subplot(211)#numrows, numcols, fignum
ax2 = fig.add_subplot(212)
ax1.plot(data['sample'],data['DATA0'],'r',
         label=header[OFFSET+0])
ax2.plot(data['sample'],data['DATA1'],'b',
         label=header[OFFSET+1])
ax1.set_title("ADC Samples")
ax1.set_xlabel('Samples')
ax1.set_ylabel('Reading')
ax2.set_xlabel('Samples')
ax2.set_ylabel('Reading')

leg1 = ax1.legend()
leg2 = ax2.legend()
plt.savefig("graph.pdf")
plt.show()
#End
