from boys import *
from girls import *
from couples import *
from input import *
from searchlist import *
from searchsortedlist import *
from searchhash import *
import csv
import logging


def writeLog(data):
    logging.basicConfig(filename='Que7.log', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info(data)


info()
boysInfo = open("boys.csv")
boysReader = csv.reader(boysInfo, delimiter='\t')
girlsInfo = open("girls.csv")
girlsReader = csv.reader(girlsInfo, delimiter='\t')

Boys = []
Girls = []
Couples = []
hashtable ={}

for i in boysReader:
    Boys += [boys(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]
for i in girlsReader:
    Girls += [girls(i[0], int(i[1]), int(i[2]), int(i[3]), i[4])]

for girl in Girls:
    for boy in Boys:
        if girl.mainCost <= boy.budget and girl.attractiveness >= boy.minRequirement and boy.status == "single":
            boy.status = "committed"
            girl.status = "committed"
            boy.girlname = girl.name
            Couples.append(couples(boy, girl))
            hashtable.update({boy.name:girl.name})
            break

boysname = []
for i in Boys:
    boysname.append(i.name)

print "To find by array/list :"
s = searchlist(boysname, Couples)
s.search()

print "To find by binarysearch :"
s= searchsortedlist(boysname,Couples)
s.search()

print "To find by hashtable"
s = searchhash(boysname,hashtable)
s.search()
