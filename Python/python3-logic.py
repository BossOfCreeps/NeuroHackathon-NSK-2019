from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'http://www.thefamouspeople.com/singers.php'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)

index = 0;
mine_index = 0
group = input("Group: ")
day = input("Day: ")
lesson = input("Lesson: ")

time="TIME:201809"
if (day.find("пони")>-1) or (day.find("Пони")>-1):
    time=time+"03"
if (day.find("втор")>-1) or (day.find("Втор")>-1):
    time=time+"04"
if (day.find("сред")>-1) or (day.find("Сред")>-1):
    time=time+"05"
if (day.find("четв")>-1) or (day.find("Четв")>-1):
    time=time+"06"
if (day.find("пятн")>-1) or (day.find("Пятн")>-1):
    time=time+"07"
if (day.find("субб")>-1) or (day.find("Субб")>-1):
    time=time+"08"
if (day.find("воск")>-1) or (day.find("Воск")>-1):
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
    

url = 'https://timetable.tusur.ru/faculties/rtf/groups/'+str(group)+'.ics'
response = http.request('GET', url)
ics = BeautifulSoup(response.data)

    index=index+1
    a = ("TTT").find("T")
    print (index)
    if (0>-1):
        mine_index = index+2
    if  (mine_index==index):
        myLine = line[8:len(line)]
        print (myLine)
