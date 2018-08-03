
"""


"""

from Flv.flv_header import *


class flv(object):
    def __init__(self):
        self.head=flv_header()
        self.tagN=[]
        self.h264data=[]
        self.aac=[]
        pass

    def tag(self):
        return self.tagN

    def head(self):
        return self.head

    def addh264(self,dat):
        self.h264data.append(dat)
    def addaac(self,acct):
        self.aac.append(acct)
    def geth264(self):
        return self.h264data
    def getacc(self):
        return self.aac

    def __repr__(self):
        print("flv class type")