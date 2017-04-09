import boys
import girls
from gifts import *
import couples
from couplegen import *
from input import *
import csv
import logging
import math


def writeLog(data):
    logging.basicConfig(filename='Que5.log', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info(data)


info()

giftsInfo = open("gifts.csv")
giftsReader = csv.reader(giftsInfo, delimiter='\t')
Gifts = []

for i in giftsReader:
    Gifts += [gifts(int(i[0]), int(i[1]), i[2])]

makecouples()

for i in range(len(Couples)):
    print Couples[i].boy.name,
    print "---",
    print Couples[i].girl.name

Gifts = sorted(Gifts, key=lambda i: i.price)

for i in xrange(len(Couples)):
    Couples[i].compatibility = Couples[i].boy.budget - Couples[i].girl.mainCost + abs(
        Couples[i].boy.attractiveness - Couples[i].girl.attractiveness) + abs(
        Couples[i].boy.intelligence - Couples[i].girl.intelligence)

for i in range(len(Couples)):
    if Couples[i].boy.category == "The Miser":
        j = 0
        k = 0
        v = 0
        while k < Couples[i].girl.mainCost and j < len(Gifts):
            k += Gifts[j].price
            v += Gifts[j].value
            j += 1
        k += Gifts[j].price
        v += Gifts[j].value
        j += 1
        Couples[i].boy.happiness = Couples[i].boy.budget - k
        Couples[i].totalPrice = k
        Couples[i].totalValue = v

    elif Couples[i].boy.category == "The Generous":
        j = len(Gifts) - 1
        k = 0
        v = 0
        while k < Couples[i].boy.budget and j > 0:
            k += Gifts[j].price
            v += Gifts[j].value
            j -= 1
        Couples[i].boy.happiness = Couples[i].girl.happiness
        Couples[i].totalPrice = k
        Couples[i].totalValue = v

    else:
        j = 0
        k = 0
        v = 0
        while k < Couples[i].girl.mainCost and j < len(Gifts):
            k += Gifts[j].price
            v += Gifts[j].value
            j += 1
        k += Gifts[j].price
        v += Gifts[j].value
        j += 1
        for l in range(j, len(Gifts)):
            if Gifts[l].category == "Luxury" and Couples[i].boy.budget - k >= Gifts[l].price:
                k += Gifts[l].price
                v += Gifts[l].price
                break
        Couples[i].boy.happiness = Couples[i].girl.intelligence
        Couples[i].totalPrice = k
        Couples[i].totalValue = v

for i in range(len(Couples)):
    if Couples[i].girl.category == "The Choosy":
        Couples[i].girl.happiness = math.log(Couples[i].totalPrice)

    elif Couples[i].girl.category == "The Normal":
        Couples[i].girl.happiness = Couples[i].totalPrice + Couples[i].totalValue

    else:
        Couples[i].girl.happiness = math.exp(Couples[i].totalPrice)

for i in xrange(len(Couples)):
    Couples[i].happiness = Couples[i].boy.happiness + Couples[i].girl.happiness


def happy(a, b):
    if a.happiness > b.happiness:
        return 1
    elif a.happiness < b.happiness:
        return -1
    else:
        return 0


Couples.sort(happy, reverse=True)

k = raw_input("Enter the value of k:")
k = int(k)
print "The " + str(k) + " most happiest couples are :"
for i in range(k):
    print Couples[i].boy.name,
    print '---',
    print Couples[i].girl.name
