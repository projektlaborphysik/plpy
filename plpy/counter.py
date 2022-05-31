# -*- coding: utf-8 -*-
"""
Bibliothek zum Betrieb verschiedener Experimente im Projektlabor Physik.

Sammlung der Funktionen für das Auswerten von Signalen eines
Geiger-Müller-Zählrohrs / Zählers. 

Version Fri May 27 14:25:55 2022
@author: Robin Krüger
"""
import os
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sounddevice as sd


def test():
    print("Der Bibliotheksteil 'counter' wurde importiert!")
    return True