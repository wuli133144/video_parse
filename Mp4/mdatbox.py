from Mp4.Box import *


class mdatbox(Box):
    def __init__(self, sz, type):
        super().__init__(sz, type)
        self.m_data=None


    def getdata(self):
        return self.m_data

    def setdata(self,dat):
        self.m_data=dat

    def __str__(self):
        return "mdat type %s size %d " % (self.gettype(),self.getsize())
        pass

