from boys import *
from girls import *
from couples import *
from input import *
import csv
import logging

def writeLog(data):
    logging.basicConfig(filename='Que3.log', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info(data)

info()

boysInfo = open("boys.csv")
boysReader = csv.reader(boysInfo, delimiter='\t')
girlsInfo = open("girls.csv")
girlsReader = csv.reader(girlsInfo, delimiter='\t')

Boys = []
Girls = []
Couples = []

for i in boysReader:
    Boys += [boys(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]
for i in girlsReader:
    Girls += [girls(i[0], int(i[1]), int(i[2]), int(i[3]), i[4])]

def makecouples():
    for i in xrange(len(Boys)+len(Girls)):
        if i%2==0:
            for girl in Girls:
                if girl.status=="single":
                    for boy in Boys:
                        if girl.mainCost <= boy.budget and girl.status == 'single' and boy.status == "single":
                            girl.status = "In relationship"
                            boy.status = "In relationship"
                            Couples.append(couples(boy,girl))
                            print girl.name +" has chosen "+boy.name +" as her boyfriend "
                            writeLog(girl.name +" has chosen "+boy.name +" as her boyfriend ")
                            break
                    if girl.status=="In relationship":
                        break
        else:
            for boy in Boys:
                beautyGirls = sorted(Girls, key = lambda i:i.attractiveness, reverse=True)
                if boy.status=="single":
                    for girl in beautyGirls:
                        if girl.status == 'single' and boy.status == "single" :
                            girl.status = "In relationship"
                            boy.status = "In relationship"
                            Couples.append(couples(boy, girl))
                            print boy.name +" has chosen "+ girl.name+" as his girlfriend"
                            writeLog(boy.name +" has chosen "+ girl.name+" as his girlfriend")
                            break
                    if boy.status=="In relationship":
                        break