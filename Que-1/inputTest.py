import csv
from random import randint as r
'''
Categories of boys:
	1.The Miser
	2.The Generous
	3.The Geek
'''	
'''Categories of girls:
	1.The Choosy
	2.The Normal
	3.The Desperate
'''
'''Categories of gifts:
	1.Essential
	2.Luxury
	3.Utility
'''
boysCategory = ["The Miser","The Generous","The Geek"]
girlsCategory = ["The Choosy", "The Normal", "The Desperate"]


def writeInfo(info, file):
	'''Method to write data in a csv file
	'''
	outputFile = open(file,"w")
	outputWriter = csv.writer(outputFile, delimiter='\t')
	for i in info:
		outputWriter.writerow(i)
	outputFile.close()

bcat=boysCategory[r(0,2)]
gcat=girlsCategory[r(0,2)]

def infoTest():
	'''gets the information of boys and girls using random generator'''
	boysInfo = []
	girlsInfo = []
	for i in xrange(50):
		x,y,z=r(0,10),r(0,10),r(0,10)
		w=r(0,100)
		boysInfo += [('b-'+str(i),x,y,w,z,bcat)]
	'''writing boys information into boysInfo.csv file'''
	writeInfo(boysInfo,"boysInfo.csv")
	for i in xrange(25):
		x,y=r(0,10),r(0,10)
		z=r(0,100)
		girlsInfo += [('g-'+str(i),x,y,z,gcat)]
	'''writing girls information into girlsInfo.csv file'''
	writeInfo(girlsInfo,"girlsInfo.csv")
