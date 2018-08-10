"""
basic script tag type
including streamdata information
jackwu
"""


from Flv.tag import        *
from Flv.utils import      *
from Flv.AMF_string import *

from Flv.AMF_array import  *

class OnMetaData(flv_tag):
    def __init__(self):
        super().__init__(FLV_FORMAT_SCRIPT)
        self.amf_string=None
        self.amf_array =None

    def setData(self,dt):
        self.data.append(dt)

    def getData(self):

        return self.data

    def getsize(self):
        return len(self.data)


