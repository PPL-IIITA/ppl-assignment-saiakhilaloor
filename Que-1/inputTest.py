import csv
from random import randint as r

boysCategory = ["The Miser","The Generous","The Geek"]
girlsCategory = ["The Choosy", "The Normal", "The Desperate"]
giftsCategory = ["Essential Gifts", "Luxury Gifts", "Utility Gifts"]


def writeInfo(info, file):
	outputFile = open(file,"w")
	outputWriter = csv.writer(outputFile, delimiter='\t')
	for i in info:
		outputWriter.writerow(i)
	outputFile.close()


def infoTest():
	boysInfo = []
	girlsInfo = []
	giftsInfo = []
	for i in xrange(50):
		boysInfo += [('boy-'+str(i),r(0,10),r(0,10),r(1,10000),r(0,10),boysCategory[r(0,2)])]
	for i in xrange(25):	
		girlsInfo += [('girl-'+str(i),r(0,10),r(0,10),r(1,10000),girlsCategory[r(0,2)])]
	for i in xrange(30):
		giftsInfo += [("gift-"+str(i),r(0,1000),r(0,1000),giftsCategory[r(0,2)])]
	writeInfo(boysInfo,"boysInfo.csv")
	writeInfo(girlsInfo,"girlsInfo.csv")
	writeInfo(giftsInfo,"giftsInfo.csv")