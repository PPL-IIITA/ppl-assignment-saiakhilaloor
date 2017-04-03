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
giftsCategory = ["Essential", "Luxury", "Utility"]


def writeInfo(info, file):
	'''Method to write data into a csv file'''
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
		boysInfo += [('boy-'+str(i),r(0,10),r(0,10),r(1,100),r(0,10),boysCategory[r(0,2)])]
	writeInfo(boysInfo,"boysInfo.csv")
	for i in xrange(25):	
		girlsInfo += [('girl-'+str(i),r(0,10),r(0,10),r(1,100),girlsCategory[r(0,2)])]
	writeInfo(girlsInfo,"girlsInfo.csv")
	for i in xrange(50):
		giftsInfo += [(r(1,20),r(1,10),giftsCategory[r(0,2)])]
	writeInfo(giftsInfo,"giftsInfo.csv")
