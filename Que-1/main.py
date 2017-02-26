import logging
import csv
from boys import boys
from girls import girls
from inputTest import infoTest

def writeLog(data):
	logging.basicConfig(filename='Que-1.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
	logging.info(data)

infoTest()
boysInfo=open("boysInfo.csv")
girlsInfo=open("girlsInfo.csv")
Boysreader=csv.reader(boysInfo,delimiter='\t')
Girlsreader=csv.reader(girlsInfo,delimiter='\t')

Boys=[]
Girls=[]
for i in Boysreader:
	Boys+=[boys(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])]
for i in Girlsreader:
	Girls+=[girls(i[0],int(i[1]),int(i[2]),int(i[3]),i[4])]

for girl in Girls:
	for boy in Boys:
		if girl.mainCost <= boy.budget and girl.attractiveness >= boy.minRequirement and boy.status=='single':
			girl.status = "committed"
			boy.status = "committed"
			boy.girlfriendName = girl.name 
			girl.boyfriendName = boy.name
			print girl.name,
			print boy.name
			writeLog(girl.name +" In Relationship With "+boy.name)
			break