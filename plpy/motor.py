# -*- coding: utf-8 -*-
"""
Bibliothek zum Betrieb verschiedener Experimente im Projektlabor Physik.

Funktionen zum Ansteuern von Schrittmotoren über die PL-Schrittmotorschnitstelle
(Arduino und Serielle Schnittstelle) und für die Stages der Xbox. 

Version Fri May 27 14:25:55 2022
@author: Robin Krüger
"""
import os
import numpy as np
import scipy
import time
import serial
from serial.tools import list_ports

BAUD_RATE = 9600

def test():
    print("Der Bibliotheksteil 'motor' wurde importiert!")
    return True

##----   nicht integrierte Funktionen ---###

# Auslesen und Freimachen des Buffers
# Optional kann der Inhalt ausgegeben werden
def read_complete_buffer(ser,printing=False):
    while(True):
        result = ser.readline()
        if result == b'':
            break
        if printing:
            print(result)
            
def read_complete_buffer_to_string(ser,printing=False):
    result_string = ''
    while(True):
        result = ser.readline()
        result_string += str(result)
        if result == b'':
            break
        if printing:
            print(result)
    return result_string

# Schritte mit dem Schrittmotor gehen
def go(ser,steps):
    ser.write(bytes(str(steps),'utf-8'))
    time.sleep(1)
    read_complete_buffer(ser,True)
    
# Position abfragen
def position(ser):
    read_complete_buffer(ser,False)
    ser.write(bytes('pos','utf-8'))
    time.sleep(1)
    ser.readline()
    result = ser.readline()
    result = result[9:-2]
    print(result)
    return float(result)
    
# Microstepping einstellen
#  m1 - Setzt den Motor auf ganze Schritte
#  m2 - Halbschritte
#  m4 - Viertelschritte
#  m8 - Achtelschritte
# m16 - Sechzehntelschritte
def microstep(ser,string):
    ser.write(bytes(string,'utf-8'))
    time.sleep(1)
    read_complete_buffer(ser,True)

# Serielle Schnittstellen anzeigen
def print_ports():
    schnittstellen = list_ports.comports() 
    print('Index \tName')
    for i in range(len(schnittstellen)):
        print(i,'\t',schnittstellen[i].device)
    return True

###--- nicht integrierte Funktiionen Ende ---###

def recognice_devices():
    schnittstellen = list_ports.comports() 
    print('Index \tSchnittstelle \tName')
    for i in range(len(schnittstellen)):
        ser = serial.Serial(schnittstellen[i].device, BAUD_RATE,timeout=1)
        ser.write(bytes('w','utf-8'))
        result = read_complete_buffer_to_string(ser,printing=False)
        index = result.find('device')
        identifier = result[index+6]
        print(i,'\t',schnittstellen[i].device,'\t',identifier)
    return True




    
