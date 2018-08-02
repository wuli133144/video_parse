

from Mp4.boxHeader import *


class Box(object):

    """
     details about box: include size,type

    """
    def __init__(self,sz,type):

        self.header=boxheader(sz,type,0)
        self.container=[]


    def getsize(self):
        return self.header.getsize()
    def gettype(self):
        return self.header.gettype()
    def getboxes(self):
        return self.container
    def add(self,element):
        self.container.append(element)


    def __str__(self):
        return "this box size= %d type = %s container size=%d " % (self.size,self.type,len(self.container))
