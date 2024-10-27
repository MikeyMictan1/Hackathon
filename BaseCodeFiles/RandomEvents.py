class Event:
#
    def __init__(self,text,cost,happyDec,thirstDec,hungryDec):
    #
        self.text=text
        self.cost=cost
        self.happyDec=happyDec
        self.thirstDec=thirstDec
        self.hungryDec=hungryDec
    #
    def gettext (self):
    #
        return self.text
    #
    def getcost (self):
    #
       return self.cost
    #
    def getdepression (self):
    #
        returning = {self.happyDec,self.thirstDec,self.hungryDec}
        return returning
    #
#