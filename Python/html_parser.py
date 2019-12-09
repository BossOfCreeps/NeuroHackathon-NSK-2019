#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

day = u""
week = u""
lesson = u"3"
group = u"726-1"
inputString = u""

data =""

nechet = u"нечётн"

f = open('input.txt')
for line in f:
    inputString=line

if (inputString.find(nechet)>-1):# or (inputString.find("нечетн")>-1) or (inputString.find("Нечетн")>-1) or (inputString.find("Нечётн")>-1):
    week = u"нечёт"
else:
    week = u"чёт"

if (inputString.find(" понедельн")>-1):
    day = u"пн"
if (inputString.find(" вторн")>-1):
    day = u"вт"
if (inputString.find(" сред")>-1):
    day = u"ср"
if (inputString.find(" четверг")>-1):
    day = u"чт"
if (inputString.find(" пятниц")>-1):
    day = u"пт"
if (inputString.find(" суббот")>-1):
    day = u"сб"

print week

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


f = urllib.urlopen("https://timetable.tusur.ru/faculties/"+fac+"/groups/"+group+"?week_id="+week)

print "https://timetable.tusur.ru/faculties/"+fac+"/groups/"+group+"?week_id="+week

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
