# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from gtts import gTTS
import os
import time, sys
from pygame import mixer 
import speech_recognition as sr
import urllib
import serial

sys.getdefaultencoding()
ics = urllib.urlopen("https://timetable.tusur.ru/faculties/rtf/groups/116.ics")

in_string = u"егор"
out_string = u"егор почему ничего не работает"

day = u" "
week = u" "
lesson = u" "
group = u" "
inputString = u" "

data =u""

ser = serial.Serial('COM9', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

#ser.close()             # close port

close_app = 0
mixer.init()
fileName = 1
files = os.listdir("C:\Users\Lab210\Desktop\Hackaton")
for f in files:
    if (f.find(".mp3")>-1):
        os.remove(f)

while True:
    out_string=""
    r = sr.Recognizer()
    ser.write(0)
    with sr.Microphone() as source:
        print("Say smt:")
        audio = r.listen(source)    
    try:
        in_string = r.recognize_google(audio, language="ru-RU")
        print(in_string)
    except sr.UnknownValueError:
        print("Dont understand")
        out_string=u" "
    except sr.RequestError as e:
        print("Error; {0}".format(e))


    inputString=in_string
    if (inputString.find(u"привет")>-1) or (inputString.find(u"Привет")>-1):
        out_string=u"Привет, привет, дорогой друг"
    if (inputString.find(u"пока")>-1) or (inputString.find(u"Пока")>-1):
        out_string=u"Пока, надеюсь был полезен"
        close_app=1

    nechet = u"нечет"
    inputString=in_string
    if (inputString.find(nechet)>-1):# or (inputString.find("нечетн")>-1) or (inputString.find("Нечетн")>-1) or (inputString.find("Нечётн")>-1):
        week = u"нечёт"
    else:
        week = u"чёт"

    if (inputString.find(u"понедельн")>-1) or (inputString.find(u"Понедельн")>-1):
        day = u"пн"
    if (inputString.find(u"вторн")>-1):
        day = u"вт"
    if (inputString.find(u"сред")>-1):
        day = u"ср"
    if (inputString.find(u"четверг")>-1):
        day = u"чт"
    if (inputString.find(u"пятниц")>-1):
        day = u"пт"
    if (inputString.find(u"суббот")>-1):
        day = u"сб"

    print day

    if (inputString.find(u"первая")>-1):
        lesson = u"1"
    if (inputString.find(u"вторая")>-1):
        lesson = u"2"
    if (inputString.find(u"третья")>-1):
        lesson = u"3"
    if (inputString.find(u"четвертая")>-1):
        lesson = u"4"
    if (inputString.find(u"пятая")>-1):
        lesson = u"5"
    if (inputString.find(u"шестая")>-1):
        lesson = u"6"
    if (inputString.find(u"седьмая")>-1):
        lesson = u"7"

    num_group=" "
    if (inputString.find(u"групп")>-1):
        num_group=inputString[inputString.find(u"группа")+7:len(inputString)]
        if (len(num_group)==3):
            group=num_group
        else:
            group=num_group[0:3]+"-"+num_group[3]
    print group

    if (day==u"пн") and (week == u"чёт"):
        data = u"15 окт."
    if (day==u"вт") and (week == u"чёт"):
        data = u"16 окт."
    if (day==u"ср") and (week == u"чёт"):
        data = u"17 окт."
    if (day==u"чт") and (week == u"чёт"):
        data = u"18 окт."
    if (day==u"пт") and (week == u"чёт"):
        data = u"19 окт."
    if (day==u"сб") and (week == u"чёт"):
        data = u"20 окт."

    if (day==u"пн") and (week == u"нечёт"):
        data = u"22 окт."
    if (day==u"вт") and (week == u"нечёт"):
        data = u"23 окт."
    if (day==u"ср") and (week == u"нечёт"):
        data = u"24 окт."
    if (day==u"чт") and (week == u"нечёт"):
        data = u"25 окт."
    if (day==u"пт") and (week == u"нечёт"):
        data = u"26 окт."
    if (day==u"сб") and (week == u"нечёт"):
        data = u"27 окт."

    if (week == u"нечёт"):
        week = u"426"
    else:
        week = u"425"

    time = " "
    
    if (lesson=="1"):
        time = "08:50"
    if (lesson=="2"):
        time = "10:40"
    if (lesson=="3"):
        time = "13:15"
    if (lesson=="4"):
        time = "15:00"
    if (lesson=="5"):
        time = "16:45"
    if (lesson=="6"):
        time = "18:30"
    if (lesson=="7"):
        time = "20:15"
    fac = u" "
    if (group[0]=="1"):
        fac="rtf"
    if (group[0]=="2"):
        fac="rkf"
    if (group[0]=="3"):
        fac="fet"
    if (group[0]=="4"):
        fac="fsu"
    if (group[0]=="5"):
        fac="fvs"
    if (group[0]=="6"):
        fac="gf"
    if (group[0]=="7"):
        fac="fb"
    if (group[0]=="8"):
        fac="ef"
    if (group[0]=="0") and (group[1]=="9"):
        fac="yuf"
    if (group[0]=="0") and (group[1]!="9"):
        fac="fit"

    print week
    print data
    print time

    f = urllib.urlopen("https://timetable.tusur.ru/faculties/"+fac+"/groups/"+group+"?week_id="+week)

#    print "https://timetable.tusur.ru/faculties/"+fac+"/groups/"+group+"?week_id="+week

    index = 0
    super_index = 0
    findData = 0
    stringToParse = ""
    finalString = ""

    for line in f:
        index = index+1 
        if (line.decode('utf-8').find(data)>-1) and (stringToParse == ""):
            findData = 1
        if (findData==1) and (line.decode('utf-8').find(u"<span>"+time+u"</span>")>-1):
            super_index = index + 8
            findData=0
        if (index == super_index):
            stringToParse=line
            #print line

    if (stringToParse.find("title=")!=-1):
        stingStart = stringToParse.find("title=")+7
        stringFinish = stringToParse.find(">",stingStart)-1
        finalString=stringToParse[stingStart:stringFinish]
    else:
        if (stringToParse.find("discipline")!=-1):
            stingStart = stringToParse.find("discipline")+12
            stringFinish = stringToParse.find("span",stingStart)-2
            finalString=stringToParse[stingStart:stringFinish]
        else:
            if (stringToParse.find("        <td>")>-1):
                finalString="Нет занятий"
            else:
                finalString="Произошла ошибка"
                
    print finalString.decode('utf-8')

    tts = gTTS(finalString.decode('utf-8'), lang='ru')

    if (out_string!=u""):
        tts = gTTS(out_string, lang='ru')
    
    tts.save(str(fileName)+".mp3")
    mixer.music.load(str(fileName)+".mp3")
    mixer.music.play()
    ser.write(1)     # write a string
    fileName=fileName+1
    if (close_app==1):
        sys.exit()
