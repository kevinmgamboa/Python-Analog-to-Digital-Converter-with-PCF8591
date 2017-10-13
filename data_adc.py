"""
Title: Working with I2C bus Using Wiringpi
Created on Thu Oct 10 14:49:20 2017
Modified:
@author: Kevin Machado Gamboa
Ref: Raspberry pi Cookbook 1 for python programmers. chapter 7 Pag. 203
"""
# !/usr/bin/env python3
# data_adc.py
# -----------------------------------------------------------------------------
## Importing modules and creating variables

import wiringpi      # we are importing 'wiringpi' instead of 'wiringpi2' as the tutorial said
import time


DEBUG=False
LIGHT=0;TEMP=1;EXT=2;POT=3      # Photodiode input (sence signal from pulse oximeter LEDs R&IR)   
ADC_CH=[LIGHT,TEMP,EXT,POT]     # Create a vector
ADC_ADR=0x48         # PCF8591 address
ADC_CYCLE=0x04       # Recieving signal cycle from the AIN0 to AIN4 (set 0x04 to recieve from all)
BUS_GAP=0.25         # ?
DATANAME=["0:Light","1:Temperature",
"2:External","3:Potentiometer"]

# -----------------------------------------------------------------------------
## Creating a class "device" with a constructor to initialize it

class device:
    # Constructor:
    def __init__(self,addr=ADC_ADR):
        self.NAME=DATANAME
        self.i2c = wiringpi.I2C()         # Ready to start using the I2C
        self.devADC=self.i2c.setup(addr)   # To setup with any address as (0x48 - PFC8591)
        pwrup = self.i2c.read(self.devADC) #flush powerup value

        if DEBUG==True and pwrup!=-1:
            print("ADC Ready")

        self.i2c.read(self.devADC) #flush first value
        time.sleep(BUS_GAP)
        self.i2c.write(self.devADC,ADC_CYCLE)
        time.sleep(BUS_GAP)
        self.i2c.read(self.devADC) #flush first value
# -----------------------------------------------------------------------------
## Define a function to provide a list of channel names
    def getName(self) :
        return self.NAME

# -----------------------------------------------------------------------------
## Function to return a new set of samples from the ADC channels
    def getNew(self) :
        data=[]
        for ch in ADC_CH:
            time.sleep(BUS_GAP)
            data.append(self.i2c.read(self.devADC))
        return data
# -----------------------------------------------------------------------------
## creating a test function to exercise our new device class 
## (this is only to be run when the script is executed directly)
def main():
    ADC = device(ADC_ADR)
    print (str(ADC.getName()))

    for i in range(10):
        dataValues = ADC.getNew()
        print (str(dataValues))
        time.sleep(1)

if __name__=='__main__':
    main()
    #End
