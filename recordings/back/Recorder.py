# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:30:19 2021

@author: Asus
"""

import sounddevice as sd
import scipy
import wavio
import time
import winsound as win

sampling_rate = 16000
duration = 1

print("recording will start in 5 seconds")
k = 4
for j in range(0,4):
    print("in ",k,"seconds")
    time.sleep(1)
    k = k-1

print("speak after the beeps")
for i in range(60,80):
    win.Beep(1000,1000)
    record = sd.rec(sampling_rate*duration, samplerate=sampling_rate,channels=1)
    sd.wait()
    wavio.write("recording{}.wav".format(i), record, sampling_rate,sampwidth=2)
    