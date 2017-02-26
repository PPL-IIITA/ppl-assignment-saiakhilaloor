import logging
import csv
import math
from boys import boys
from girls import girls
from gifts import gifts
from Couples import Couples
from inputTest import infoTest

'''Method to write data into a log file
'''
def writeLog(data):
	logging.basicConfig(filename='Que-2.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
	logging.info(data)

infoTest()
'''Reading boys information from csv file'''
boysInfo=open("boysInfo.csv")
Boysreader=csv.reader(boysInfo,delimiter='\t')
'''Reading girls information from csv file'''
girlsInfo=open("girlsInfo.csv")
Girlsreader=csv.reader(girlsInfo,delimiter='\t')
'''Reading gifts information from csv file'''
giftsInfo =open("giftsInfo.csv")
Giftsreader=csv.reader(giftsInfo,delimiter='\t')

couples=[]
Boys=[]
Girls=[]
Gifts=[]

for i in Boysreader:
	Boys+=[boys(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])]
for i in Girlsreader:
	Girls+=[girls(i[0],int(i[1]),int(i[2]),int(i[3]),i[4])]
for i in Giftsreader:
	Gifts+=[gifts(int(i[0]),int(i[1]),i[2])]
'''Sorting gifts according to the price of the gifts in ascending order
'''
Gifts = sorted(Gifts,key = lambda a : a.price)
giftsPrice=[]
for i in Gifts:
	giftsPrice.append(i.price)

for girl in Girls:
	for boy in Boys:
		'''Matching girls with boys based on the requirements of both 
		boy and girl
		Requirements:
		1.girl.maintenanceCost <= boy.budget 
		2.girl.attractiveness >= boy.minRequirements
		3.boy.status=single
		4.gir.status=single
		'''
		if girl.mainCost <= boy.budget and girl.attractiveness >= boy.minRequirement and boy.status=='single':
			girl.status = "committed"
			boy.status = "committed"
			girl.boyfriendName = boy.name
			boy.girlfriendName = girl.name
			couples.append(Couples(boy,girl))
			writeLog(girl.name +" is in Relationship With "+boy.name)
			break

for i in range(len(couples)):
	'''Calculating the boy's happiness if boy is a Miser
	'''
	if couples[i].boy.category == "The Miser":
		j=0
		k=0
		while k<couples[i].girl.mainCost and j<len(giftsPrice):
			k+=giftsPrice[j]
			j+=1
		gift_array=[]
		for gift in Gifts :
			if j>0:
				gift_array.append(gift)
				print couples[i].boy.name+" gave "+gift.category+" type gift worth "+str(gift.price)+" to "+couples[i].girl.name
				writeLog(couples[i].boy.name+" gave "+gift.category+" type gift worth "+str(gift.price)+" to "+couples[i].girl.name)
				j-=1
		couples[i].totalgiftcost = k
		couples[i].gift=gift_array
		couples[i].boy.happiness=couples[i].boy.budget-k
		'''Calculating the boy's happiness if boy is generous
		'''
	elif couples[i].boy.category== "The Generous":
		j=0
		k=0
		while k<=couples[i].boy.budget and j < len(giftsPrice) :
			k+=giftsPrice[j]
			j+=1
		gift_array=[]
		for gift in Gifts:
			if j>0:
				gift_array.append(gift)
				writeLog(couples[i].boy.name+" gave "+gift.category+" type gift worth "+str(gift.price)+" to"+couples[i].girl.name)
				print couples[i].boy.name+" gave "+gift.category+" type gift worth "+str(gift.price)+" to "+couples[i].girl.name
				j-=1
		couples[i].totalgiftcost = k
		couples[i].gift=gift_array
		couples[i].boy.happiness=couples[i].girl.happiness
		'''Calculating the boy's happiness if boy is a geek
		'''
	else:
		j=0
		k=0
		while k<couples[i].girl.mainCost and j<len(giftsPrice):
			k+=giftsPrice[j]
			j+=1
		y=couples[i].boy.budget-k
		for x in Gifts:
			if x.category=="Luxury":
				if x.price<y:
					k+=x.price
		gift_array=[]
		for gift in Gifts :
			if j>0:
				gift_array.append(gift)
				writeLog(couples[i].boy.name+" gave "+gift.category+" type gift worth "+str(gift.price)+" to "+couples[i].girl.name)
				print couples[i].boy.name+" gave "+gift.category+" type gift worth "+str(gift.price)+" to "+couples[i].girl.name
				j-=1
		couples[i].totalgiftcost = k
		couples[i].gift=gift_array
		couples[i].boy.happiness=couples[i].girl.intelligence

for i in range(len(couples)):
	'''Calculating the girl's happiness if girl is choosy
	'''
	if couples[i].girl.category=="The Choosy":
		s=couples[i].totalgiftcost
		s=math.log(s)
		couples[i].girl.happiness=s
		'''Calculating the girl's happiness if girl is normal
		'''
	elif couples[i].girl.category=="The Normal":
		s=couples[i].totalgiftcost
		for j in couples[i].gift:
			s+=j.value
		couples[i].girl.happiness=s
		'''Calculating the girl's happiness if girl is desperate
		'''
	else:
		s=math.exp(couples[i].totalgiftcost)
		couples[i].girl.happiness=s

for i in range(len(couples)):
	'''Calculating the happiness and compatibility of the couples
	'''
	couples[i].happiness=couples[i].girl.happiness+couples[i].boy.happiness
	couples[i].compatibility = couples[i].boy.budget - couples[i].girl.mainCost +abs(couples[i].boy.attractiveness - couples[i].girl.attractiveness)+abs(couples[i].boy.intelligence - couples[i].girl.intelligence)

def happy(a, b) :
			if a.happiness > b.happiness :
				return 1
			elif a.happiness < b.happiness :
					return -1
			else :
					return 0
'''Method to sort couples based on the happiness of the couple
	couple.happiness=boy.happiness + girl.happiness
'''
couples.sort(happy)
print "**** The Happiest Couples in decreasing order are ****"
for i in range(len(couples)-1,-1,-1):
	print couples[i].boy.name,
	print '<--->',
	print couples[i].girl.name

def compatible (a, b):
		if (a.compatibility > b.compatibility):
			return 1
		elif a.compatibility < b.compatibility:
			return -1
		else :
			return 0

'''Method to sort couples based on the happiness of the couple
	couple.compatibility=boy.budget-girl.maintenanceCost + abs(girl.attractiveness-boy.attractiveness)+abs(girl.intelligence-boy.intelligence)
'''
couples.sort(compatible)
print "**** The Compatible Couples in decreasing order are ****"
for i in range(len(couples)-1,-1,-1):
	print couples[i].boy.name,
	print '<--->',
	print couples[i].girl.name






