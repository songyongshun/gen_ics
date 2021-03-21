# coding: utf-8
#!/usr/bin/python

import sys
import time, datetime
import json
from random import Random


__author__ = 'ys_song'
__site__ = 'ys_song@foxmail.com'

checkFirstWeekDate = 0
checkReminder = 1

YES = 0
NO = 1

DONE_firstWeekDate = time.time()
DONE_reminder = ""
DONE_EventUID = ""
DONE_UnitUID = ""
DONE_CreatedTime = ""
DONE_ALARMUID = ""


classTimeList = []
classInfoList = []

def main():
    
	basicSetting();
	uniteSetting();
	#thingInfoHandle();
	icsCreateAndSave();

def classICSCreate(classInfo):
	global classTimeList, DONE_ALARMUID, DONE_UnitUID
	i = int(classInfo["classTime"]-1)
	className = classInfo["className"]+"|"+classTimeList[i]["name"]+"|"+classInfo["classroom"]
	endTime = classTimeList[i]["endTime"]
	startTime = classTimeList[i]["startTime"]
	for date in classInfo["date"]:
		eventString = "BEGIN:VEVENT\nCREATED:"+classInfo["CREATED"]
		eventString = eventString+"\nUID:"+classInfo["UID"]
		eventString = eventString+"\nDTEND;TZID=Asia/Shanghai:"+date+"T"+endTime
		eventString = eventString+"00\nTRANSP:OPAQUE\nX-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC\nSUMMARY:"+className
		eventString = eventString+"\nDTSTART;TZID=Asia/Shanghai:"+date+"T"+startTime+"00"
		eventString = eventString+"\nDTSTAMP:"+DONE_CreatedTime
		eventString = eventString+"\nSEQUENCE:0\nBEGIN:VALARM\nX-WR-ALARMUID:"+DONE_ALARMUID
		eventString = eventString+"\nUID:"+DONE_UnitUID
		eventString = eventString+"\nTRIGGER:"+DONE_reminder
		eventString = eventString+"\nDESCRIPTION:事件提醒\nACTION:DISPLAY\nEND:VALARM\nEND:VEVENT\n"
		return eventString
	print("classICSCreate")		
	

def save(string):
     f = open("half_hour.ics", 'wb')
     f.write(string.encode("utf-8"))
     f.close()

def icsCreateAndSave():
	icsString = "BEGIN:VCALENDAR\nMETHOD:PUBLISH\nVERSION:2.0\nX-WR-CALNAME:half_hour\nPRODID:-//Apple Inc.//Mac OS X 10.12//EN\nX-APPLE-CALENDAR-COLOR:#FC4208\nX-WR-TIMEZONE:Asia/Shanghai\nCALSCALE:GREGORIAN\nBEGIN:VTIMEZONE\nTZID:Asia/Shanghai\nBEGIN:STANDARD\nTZOFFSETFROM:+0900\nRRULE:FREQ=YEARLY;UNTIL=19910914T150000Z;BYMONTH=9;BYDAY=3SU\nDTSTART:19890917T000000\nTZNAME:GMT+8\nTZOFFSETTO:+0800\nEND:STANDARD\nBEGIN:DAYLIGHT\nTZOFFSETFROM:+0800\nDTSTART:19910414T000000\nTZNAME:GMT+8\nTZOFFSETTO:+0900\nRDATE:19910414T000000\nEND:DAYLIGHT\nEND:VTIMEZONE\n"
	global DONE_CreatedTime, DONE_EventUID
	CreateTime()
	#thingList["CREATED"] = DONE_CreatedTime
	#thingList["DTSTAMP"] = DONE_CreatedTime
	UID_List = []
	# for date in dateList:
	# 	UID_List.append(UID_Create())
	# thingList["UID"] = UID_List

	global thingTimeList, DONE_ALARMUID, DONE_UnitUID
	eventString = ""
	#string = startDate.strftime('%Y%m%d')
	#index = 0


	for thing in thingList :
#		UID_List.append(UID_Create())

		startDate = datetime.datetime.fromtimestamp(int(time.mktime(DONE_firstWeekDate))) + datetime.timedelta(0)
		string = startDate.strftime('%Y%m%d')
		thing["UID"] = UID_Create()
		thing["CREATED"] = DONE_CreatedTime
		thing["DTSTAMP"] = DONE_CreatedTime
		startTime = json.dumps(thing["Time"])[1:7]
		thing_info = json.dumps(thing["Thing"],ensure_ascii=False)
		thingInfo = thing_info.replace('"','')
		#print(thingInfo)

		time_tmp1 = time.strptime(string+startTime,'%Y%m%d%H%M%S')
		#print(time_tmp1)
		time_tmp2 = datetime.datetime.fromtimestamp(int(time.mktime(time_tmp1))) + datetime.timedelta(days = 0, minutes = 30)
		endTime = time_tmp2.strftime('%H%M%S')

		eventString = eventString+"BEGIN:VEVENT\nCREATED:"+thing["CREATED"]
		eventString = eventString+"\nUID:"+thing["UID"]
		eventString = eventString+"\nDTEND;TZID=Asia/Shanghai:"+string+"T"+endTime
		eventString = eventString+"\nTRANSP:OPAQUE\nX-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC\nSUMMARY:"+thingInfo
		eventString = eventString+"\nDTSTART;TZID=Asia/Shanghai:"+string+"T"+startTime
		eventString = eventString+"\nDTSTAMP:"+DONE_CreatedTime
		eventString = eventString+"\nSEQUENCE:0\nBEGIN:VALARM\nX-WR-ALARMUID:"+DONE_ALARMUID
		eventString = eventString+"\nUID:"+DONE_UnitUID
		eventString = eventString+"\nTRIGGER:"+DONE_reminder
		eventString = eventString+"\nDESCRIPTION:事件提醒\nACTION:DISPLAY\nEND:VALARM\nEND:VEVENT\n"

		#index += 1

	icsString = icsString + eventString + "END:VCALENDAR"
	save(icsString)
	print("icsCreateAndSave")


def UID_Create():
	return random_str(20) + "ys_song0520"


def CreateTime():
	# 生成 CREATED
	global DONE_CreatedTime
	date = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
	DONE_CreatedTime = date + "Z"
	# 生成 UID
	# global DONE_EventUID
	# DONE_EventUID = random_str(20) + "&Chanjh.com"

	print("CreateTime")

def uniteSetting():
	# 
	global DONE_ALARMUID
	DONE_ALARMUID = random_str(30) + "ys_song0520"
	# 
	global DONE_UnitUID
	DONE_UnitUID = random_str(20) + "ys_song0520"
	print("uniteSetting")

def setThingInfo():
	data = []
	with open('conf_thingsInfo.json', 'r', encoding="utf-8") as f:
		data = json.load(f)
		print(data)
	global thingList
	
	thingList = data["thingsInfo"]
	print("setThingInfo:")
	

def setFirstWeekDate(firstDay):
	global DONE_firstWeekDate
	DONE_firstWeekDate = time.strptime(firstDay,'%Y%m%d')
	print("setFirstWeekDate:",DONE_firstWeekDate)

def setReminder(reminder):
	global DONE_reminder
	reminderList = ["-PT10M","-PT30M","-PT1H","-PT2H","-P1D"]
	if(reminder == "1"):
		DONE_reminder = reminderList[0]
	elif(reminder == "2"):
		DONE_reminder = reminderList[1]
	elif(reminder == "3"):
		DONE_reminder = reminderList[2]
	elif(reminder == "4"):
		DONE_reminder = reminderList[3]
	elif(reminder == "5"):
		DONE_reminder = reminderList[4]
	else:
		DONE_reminder = "NULL"


	print("setReminder",reminder)

def checkReminder(reminder):
	# TODO

	print("checkReminder:",reminder)
	List = ["0","1","2","3","4","5"]
	for num in List:
		if (reminder == num):
			return YES
	return NO

def checkFirstWeekDate(firstWeekDate):
	# 长度判断
	if(len(firstWeekDate) != 8):
		return NO;
	
	year = firstWeekDate[0:4]
	month = firstWeekDate[4:6]
	date = firstWeekDate[6:8]
	dateList = [31,29,31,30,31,30,31,31,30,31,30,31]

	# 年份判断
	if(int(year) < 1970):
		return NO
	# 月份判断
	if(int(month) == 0 or int(month) > 12):
		return NO;
	# 日期判断
	if(int(date) > dateList[int(month)-1]):
		return NO;

	print("checkFirstWeekDate:",firstWeekDate)
	return YES

def basicSetting():
	info = "欢迎使用课程表生成工具。\n接下来你需要设置一些基础的信息方便生成数据\n"
	print (info)
	
	info = "请设置开始那天的日期(如：20160905):\n"
	firstDay = input(info)
#	firstWeekDate = input(info)
#	checkInput(checkFirstWeekDate, firstWeekDate)
	checkInput(checkFirstWeekDate, firstDay)
	info = "正在配置half_hour信息……\n"
	print(info)
	try :
		setThingInfo()
		print("配置half_hour信息完成。\n")
	except :
		sys_exit()
	print("here!!!")
	info = "正在配置提醒功能，请输入数字选择提醒时间\n【0】不提醒\n【1】前 10 分钟提醒\n【2】前 30 分钟提醒\n【3】前 1 小时提醒\n【4】前 2 小时提醒\n【5】前 1 天提醒\n"
	reminder = input(info)
	checkInput(checkReminder, reminder)

def checkInput(checkType, input):
	if(checkType == checkFirstWeekDate):
		if (checkFirstWeekDate(input)):
			info = "输入有误，请重新输入第一周的星期一日期(如：20160905):\n"
			firstWeekDate = input(info)
			checkInput(checkFirstWeekDate, firstWeekDate)
		else:
			setFirstWeekDate(input)
	elif(checkType == checkReminder):
		if(checkReminder(input)):
			info = "输入有误，请重新输入\n【1】上课前 10 分钟提醒\n【2】上课前 30 分钟提醒\n【3】上课前 1 小时提醒\n【4】上课前 2 小时提醒\n【5】上课前 1 天提醒\n"
			reminder = input(info)
			checkInput(checkReminder, reminder)
		else:
			setReminder(input)

	else:
		print("程序出错了……")
		end

def random_str(randomlength):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
def sys_exit():
	print("配置文件错误，请检查。\n")
	sys.exit()

main()