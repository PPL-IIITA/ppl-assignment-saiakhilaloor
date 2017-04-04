from random import randint as r
import csv

boysCategory = ["The Miser","The Generous","The Geek"]
girlsCategory = ["The Choosy", "The Normal", "The Desperate"]
giftsCategory = ["Essential", "Luxury", "Utility"]

def writeInfo(info, file):
    outputFile = open(file,"w")
    outputWriter = csv.writer(outputFile, delimiter='\t')
    for i in info:
        outputWriter.writerow(i)
    outputFile.close()


def info():
    boysInfo = []
    girlsInfo = []
    giftsInfo = []
    for i in xrange(50):
        boysInfo += [('boy-'+str(i),r(0,10),r(0,10),r(1,100),r(0,10),boysCategory[r(0,2)])]
    writeInfo(boysInfo,"boys.csv")
    for i in xrange(25):
        girlsInfo += [('girl-'+str(i),r(0,10),r(0,10),r(1,100),girlsCategory[r(0,2)])]
    writeInfo(girlsInfo,"girls.csv")
    for i in xrange(50):
        giftsInfo += [(r(1,20),r(1,10),giftsCategory[r(0,2)])]
    writeInfo(giftsInfo,"gifts.csv")