# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from gtts import gTTS
import os
import time, sys
from pygame import mixer 
import speech_recognition as sr
import urllib
sys.getdefaultencoding()
ics = urllib.urlopen("https://timetable.tusur.ru/faculties/rtf/groups/116.ics")

in_string = "егор"
out_string = u"егор почему ничего не работает"
close_app = 0
mixer.init()
fileName = 1
files = os.listdir("C:\Users\Lab210\Desktop\Hackaton")
for f in files:
    if (f.find(".mp3")>-1):
        os.remove(f)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say smt:")
        audio = r.listen(source)    
    try:
        in_string = r.recognize_google(audio, language="ru-RU")
        print(in_string)
    except sr.UnknownValueError:
        print("Dont understand")
        out_string=u"Я вас не понимаю"
    except sr.RequestError as e:
        print("Error; {0}".format(e))

    if (in_string.find(u"привет")>-1) or (in_string.find(u"Привет")>-1):
        out_string=u"Привет, привет, дорогой друг"
    if (in_string.find(u"пока")>-1) or (in_string.find(u"Пока")>-1):
        out_string=u"Пока, надеюсь был полезен"
        close_app=1

    index = 0;
    mine_index = 0
    for line in ics:
        index=index+1
        a=line.decode('utf-8').find(u"20180908T131500")
        if (a>-1):
            mine_index = index+2
        if  (mine_index==index):
            out_string = line[8:len(line)].decode('utf-8')

    
    tts = gTTS(out_string, lang='ru')
    tts.save(str(fileName)+".mp3")
    mixer.music.load(str(fileName)+".mp3")
    mixer.music.play()
    time.sleep(5)
    fileName=fileName+1
    if (close_app==1):
        sys.exit()
    
