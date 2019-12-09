# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gtts import gTTS
from pygame import mixer 
from mutagen.mp3 import MP3
#from pydub import AudioSegment
from math import ceil
from os import startfile
import serial, time, os, threading, math, socket

a=0

def func (t):
    global a
    arduino = serial.Serial('COM7', 9600, timeout=.1)
    mixer.init()
    tts = gTTS(text=t, lang='ru')
    tts.save(str(a)+".mp3")
    
    #speed = 1/1
    #sound = AudioSegment.from_file("good.mp3", format="mp3")
    #sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    #sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate).export('new.mp3', format='mp3')
    
    audioLenght = math.floor(MP3(str(a)+".mp3").info.length)
    
    #mixer.music.load('new.mp3')
    mixer.music.load(str(a)+".mp3")
    mixer.music.play()

    delay =  0.14
    shag = (ceil(audioLenght/delay/2))

    i = -2
    while shag>i:
        i=i+1
        arduino.write("1".encode())
        time.sleep(delay)
        arduino.write("0".encode())
        time.sleep(delay)
    a=a+1
    arduino.close()

    
print(str(a)+".mp3")
while (True):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 8005))
    data = sock.recv(1024)
    try:
        val = data[0]-48
        print(val)
        if (True):
            val = data[0]-48
            if (val==1):
                func('Стихотворение. Агния Барто - Мишка. Уронили мишку на пол, Оторвали мишке лапу. Все равно его не брошу - Потому что он.')
            if (val==2):
                func('Песня')
                mixer.init()
                mixer.music.load("music.wav")
                mixer.music.play()
            if (val==3):
                func('Мультик')
                startfile("cartoon.mp4")
            if (val==4):
                func('Зарядка. Повороты головы вправо и влево. Наклоны головы вперёд и назад, вправо и влево. Медленные круговые вращения головой.')
            if (val==5):
                func('Загадки. Какие красавцы Всегда и везде На суше родятся — Живут на воде?')

            if (val==6):
                func('Хороший')
            if (val==7):
                func('В горошек')
            if (val==8):
                func('Проросший')
            if (val==9):
                func('Засохший')

                
            if (val==17):
                func('Рыбы')
            if (val==18):
                func('Корабли')
            if (val==19):
                func('Моряки')
            if (val==20):
                func('Водоросли')
    except:
        a=1
    
    sock.close()
