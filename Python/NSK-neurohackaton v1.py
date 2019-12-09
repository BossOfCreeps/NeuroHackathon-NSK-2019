# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import serial, time
from gtts import gTTS
import os
from pygame import mixer 
import threading


def func (t):
    arduino = serial.Serial('COM10', 9600, timeout=.1)

    mixer.init()
    tts = gTTS(text=t, lang='ru')
    tts.save('good.mp3')
    mixer.music.load('good.mp3')
    mixer.music.play()

    i = 0
    s = 0.5
    while 18>i:
        i=i+1
        arduino.write("1".encode())
        time.sleep(s)
        arduino.write("0".encode())
        time.sleep(s)
        print (i)
    arduino.close()


func('Съешь ещё этих мягких французских булок, да выпей же чаю')
