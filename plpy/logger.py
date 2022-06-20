# -*- coding: utf-8 -*-
"""
Bibliothek zum Betrieb verschiedener Experimente im Projektlabor Physik.

Loggen der aactivitäten während des Experiments. 

Version Fri May 27 14:25:55 2022
@author: Robin Krüger
"""
import os
import numpy as np
import scipy
import time

logger_active = False
logger_path_default = r'C:\Users\mail\Desktop\Bibliothek - plpy\plpy\logger_folder'
logger_path   = logger_path_default




def test():
    print("Der Bibliotheksteil 'motor' wurde importiert!")
    return True

def timestamp():
    return '[XXX]'

def log():
    return True
    