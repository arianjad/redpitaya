#! /usr/bin/python

import sys
import time
import redpitaya_scpi as scpi
# redpitaya_scpi.py is used to connect to the SCPI server

ip = '169.254.174.98'
# Get IP by typing arp -a in cmd line and looking for RP MAC address 
# Can also include ip as an argument when calling this script, use sys.argv

rp_s = scpi.scpi(ip)
# Initialize connection

class AnalogOut:
	def __init__(self,sourceNum,waveform,freq)
		self.source = str(sourceNum)




def LedOn(led):
    rp_s.tx_txt('DIG:PIN LED' + str(led) + ',' + str(1))
    return
    
def LedOff(led):
    rp_s.tx_txt('DIG:PIN LED' + str(led) + ',' + str(0))
    return
# Define LED control functions
# Room for improvement: turn on multiple LEDs

def ConfigWaveForm(sourceNum,waveform):
	rp_s.tx_txt('SOUR'+str(sourceNum)+':'+'FUNC '+waveform.upper())
	print('Output ' + str(sourceNum)+' has been set to ' + waveform)
	return

def EnableOut(sourceNum):
	rp_s.tx_txt('OUTPUT' +str(sourceNum)+':STATE ON')
	print('Output ' + str(sourceNum)+' has been enabled')
	return

def DisableOut():
	rp_s.tx_txt('OUTPUT' +str(sourceNum)+':STATE OFF')
	print('Output ' + str(sourceNum)+' has been disabled')
	return

def ConfigFreq(sourceNum,)


def ConfigGenerator(sourceNum,waveform,freq,ampl,burst):
	source='SOUR'+str(sourceNumber)
	rp_s.tx_txt('GEN:RST')
	rp_s.tx_txt(FormatMessage(source,''))
