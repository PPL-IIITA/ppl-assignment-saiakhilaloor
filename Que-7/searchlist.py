import logging

def writeLog(data):
    logging.basicConfig(filename='Que3.log', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info(data)

class searchlist:
    def __init__(self,boys,Couples):
        self.boys=boys
        self.Couples = Couples

    def search(self):
        for boy in self.boys:
            flag=0
            for couple in self.Couples:
                if boy==couple.boy.name:
                    print 'The girlfriend of '+boy+" is "+couple.girl.name
                    writeLog('The girlfriend of '+boy+" is "+couple.girl.name)
                    flag=1
                    break
            if flag==0:
                print boy+" has no girl friend"
                writeLog(boy+" has no girl friend")


