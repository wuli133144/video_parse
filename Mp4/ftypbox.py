
from Mp4.Box import  *


class ftypbox(Box):

    def __init__(self,sz,type):
        Box.__init__(self,sz,type)
        self.major_brand=""
        self.minor_version=""
        self.compatible_brand=""
        pass

    def get_major_branch(self):
        return self.major_brand
    def set_major_branch(self,st):
        self.major_brand=st

    def get_minor_branch(self):
        return self.minor_version

    def set_minor_version(self, st):
        self.minor_version = st

    def get_compatible_brand(self):
        return self.compatible_brand

    def set_compatible_brand(self, st):
         self.compatible_brand = st


    def __str__(self):

        return "major branch %s minor version %s compatible branch %s" %(self.major_brand,self.minor_version,self.compatible_brand)
