



class boxheader(object):

    def __init__(self,sz,ty,lz):
        self.size=sz
        self.type=ty
        self.largesize=lz #if size=1 ->largesize


    def getsize(self):
        return self.size
    def gettype(self):
        return type

    def setlargesize(self,sz):
        self.largesize=sz
    def getlargesize(self):
        return self.largesize

    def __str__(self):
        return "box header infomation size %d type %s" %(self.getsize(),self.gettype())
