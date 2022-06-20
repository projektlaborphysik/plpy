# -*- coding: utf-8 -*-
"""
Test/Beispiele der Funktionen aus der plpy Bilbiothek.
Version Fri May 27 14:25:55 2022
@author: Robin Krüger
"""

import plpy as pl

pl.camera.test()
pl.counter.test()
pl.motor.test()
pl.logger.test()

print(pl.version)

pl.motor.recognice_devices()

#%%


print(pl.motor.BAUD_RATE)
