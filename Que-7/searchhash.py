import logging

def writeLog(data):
    logging.basicConfig(filename='Que3.log', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info(data)

class searchhash:
    def __init__(self,boys,hashtable):
        self.boys = boys
        self.hashtable = hashtable

    def search(self):
        for boy in self.boys:
            if boy in self.hashtable:
                print "The girlfriend of "+boy+" is "+self.hashtable[boy]
            else:
                print boy+" has no girlfriend"
