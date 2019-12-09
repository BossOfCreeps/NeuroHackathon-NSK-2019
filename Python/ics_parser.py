import urllib
index = 0;
mine_index = 0

day = ""

group = raw_input("Group: ")
day = raw_input("Day: ")
lesson = input("Lesson: ")

time="TIME:201809"
if (day.decode('utf-8').find("mon")>-1) or (day.decode('utf-8').find("Mon")>-1):
    time=time+"03"
if (day.decode('utf-8').find("tue")>-1) or (day.decode('utf-8').find("Tue")>-1):
    time=time+"04"
if (day.decode('utf-8').find("wed")>-1) or (day.decode('utf-8').find("Wed")>-1):
    time=time+"05"
if (day.decode('utf-8').find("thu")>-1) or (day.decode('utf-8').find("Thu")>-1):
    time=time+"06"
if (day.decode('utf-8').find("fri")>-1) or (day.decode('utf-8').find("Fri")>-1):
    time=time+"07"
if (day.decode('utf-8').find("sat")>-1) or (day.decode('utf-8').find("Sat")>-1):
    time=time+"08"
if (day.decode('utf-8').find("sun")>-1) or (day.decode('utf-8').find("Sun")>-1):
    time=time+"09"

if (str(lesson)=="1"):
    time=time+"T085000"
if (str(lesson)=="2"):
    time=time+"T104000"
if (str(lesson)=="3"):
    time=time+"T131500"
if (str(lesson)=="4"):
    time=time+"T150000"
if (str(lesson)=="5"):
    time=time+"T164500"
if (str(lesson)=="6"):
    time=time+"T183000"
if (str(lesson)=="7"):
    time=time+"T201500"
    
ics = urllib.urlopen("https://timetable.tusur.ru/faculties/rtf/groups/"+str(group)+".ics")
print "https://timetable.tusur.ru/faculties/rtf/groups/"+str(group)+".ics"
print time
for line in ics:
    index=index+1
    a=line.find(time)
    if (a>-1):
        print str(a)+" "+str(index)
        mine_index = index+2
    if  (mine_index==index):
        print line
        myLine = line[8:len(line)]
        print myLine.decode('utf-8')
