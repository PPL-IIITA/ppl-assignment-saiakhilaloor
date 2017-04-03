import logging
import csv
from boys import boys
from girls import girls
from inputTest import infoTest

'''Method for wrting into a log file for debugging '''
def writeLog(data):
	logging.basicConfig(filename='Que-1.log',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
	logging.info(data)

class Que1:
	
	def main(self):
		infoTest()
		''' reading boys and girls information'''
		boysInfo=open("boysInfo.csv")
		Boysreader=csv.reader(boysInfo,delimiter='\t')
		girlsInfo=open("girlsInfo.csv")
		Girlsreader=csv.reader(girlsInfo,delimiter='\t')
	
		Boys=[]
		Girls=[]
		for i in Boysreader:
			name=i[0]
			intelligence=int(i[1])
			attractiveness=int(i[2])
			budget=int(i[3])
			minRequirement=int(i[4])
			category=i[5]
			'''This method adds boys object'''
			Boys+=[boys(name,intelligence,attractiveness,budget,minRequirement,category)] 
		for i in Girlsreader:
			name=i[0]
			intelligence=int(i[1])
			attractiveness=int(i[2])
			mainCost=int(i[3])
			category=i[4]
			'''This method adds girls object'''
			Girls+=[girls(name,intelligence,attractiveness,mainCost,category)]   

		for girl in Girls:
			for boy in Boys: 
				'''matching boys and girls based on their criteria and requirements '''
				if girl.mainCost <= boy.budget and girl.attractiveness >= boy.minRequirement and boy.status=='single':
					''' Changing the status of the girl'''
					girl.status = "committed" 
					''' Changing status of the boy'''
					boy.status = "committed"  
					print girl.name,
					print "<--->",
					print boy.name
					writeLog(girl.name +" In Relationship With "+boy.name)
					break
			
		for girl in Girls:
			if girl.status=="single":
				writeLog(girl.name + " is Single")
			
		for boy in Boys:
			if boy.status=="single":
				writeLog(boy.name + " is Single")
			
if __name__ == '__main__':
    Que1().main()
