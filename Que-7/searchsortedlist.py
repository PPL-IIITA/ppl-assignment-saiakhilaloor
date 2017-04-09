import logging

def writeLog(data):
    logging.basicConfig(filename='Que3.log', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info(data)

class searchsortedlist:
    def __init__(self,boys,Couples):
        self.boys = boys
        self.Couples = sorted(Couples, key=lambda i:i.boyname )

    def binarysearch(self,a,value):
        self.start= 0
        self.end = len(a)-1
        self.ans = -1
        self.found = 0
        while self.start < self.end  and not self.found:
            self.mid = (self.start+self.end)/2
            if a[self.mid].boy.name == value:
                self.ans = self.mid
                self.found = 1
            elif a[self.mid].boy.name<value:
                self.start = self.mid+1

            else:
                self.end = self.mid-1

        return self.ans

    def search(self):
        for boy in self.boys:
            if self.binarysearch(self.Couples,boy) != -1:
                print "The girlfriend of "+boy+" is "+ self.Couples[self.binarysearch(self.Couples,boy)].girl.name
                writeLog("The girlfriend of "+boy+" is "+ self.Couples[self.binarysearch(self.Couples,boy)].girl.name)
            else:
                print boy + " has no girlfriend"
                writeLog(boy + " has no girlfriend")

