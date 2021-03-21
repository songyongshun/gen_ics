# coding: utf-8
#!/usr/bin/python

import csv

__author__ = 'ys_song'
__site__ = 'ys_song@foxmail.com'

# 指定信息在 csv 文件内的列数
_colOfTime = 0
_colOfThings = 1

def main():
	# 基础信息
	timeList = []
	thingList = []

	# 读取 csv 文件
	with open('half_hour.csv','r', encoding="utf-8") as f:
		lines=csv.reader(f,delimiter=' ')
		for line in lines:
			#print(mytime)
			mytime = line[0].replace(":","")
			#print(len(mytime1))
			if(len(mytime)==3) :
				timeList.append("0"+mytime+"00")
			else :
				timeList.append(mytime+"00")

#			timeList.append(line[0])
			thingList.append(line[1])

	headStr = '{\n"thingsInfo":[\n'
	tailStr = ']\n}'
	thingsInfoStr = ''
	thingsInfoArray = []


	# 确定配置内容
	info = "\n欢迎使用half_hour日历生成工具·txt2json 工具。\n这是你的 txt 文件信息配置，请检查。\n\n如若有误，请自行编辑 txtReader.py 文件第 53～54 行\n\n"
	info += "time: " + str(_colOfTime) + "列\n"
	info += "things: " + str(_colOfThings) + "列\n"

	print (info)
	# info += "输入 0 继续，输入 1 退出："
	option = input("输入 0 继续，输入其他内容退出：")
	if option == "1":
		sys.exit()
	

	# 开始操作
	thingsInfoStr += headStr
	i = 0
	for Time in timeList:
		itemthingsInfoStr = ""
		itemthingsInfoStr += '{\n' + '"Time": "' + Time + '",\n'
		itemthingsInfoStr += '"Thing": "' + thingList[i] + '"\n' + '}'

		thingsInfoStr += itemthingsInfoStr
		if i!=len(timeList)-1 :
			thingsInfoStr += ","
		i += 1
	thingsInfoStr += tailStr
	# print thingsInfoStr
	with open('conf_thingsInfo.json','wb') as f:
		f.write(thingsInfoStr.encode("utf-8"))
		f.close()
	print("\nALL DONE !")

main()