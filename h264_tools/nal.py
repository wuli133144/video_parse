



class nal(object):


    def __init__(self):
        self.startcode               =0
        self.forbidden_bit           =0        #0 express ok
        self.nal_reference_bit       =None
        self.nal_unit_type           =None
        self.rbsp                    =[]



    def __init__(self,forbidden,reference,unittype,startcode):
        self.forbidden_bit            =forbidden
        self.nal_reference_bit        =reference
        self.nal_unit_type            =unittype
        self.rbsp                     =[]
        self.startcode                =startcode


    def setforbidden_bit(self,bit):
        self.forbidden_bit            =bit

    def getforbidden_bit(self):
        return self.forbidden_bit

    def setnal_reference_bit(self,bit):
        self.nal_reference_bit        =bit

    def getnal_reference_bit(self):
        return self.nal_reference_bit

    def setnal_unit_type(self,bit):
        self.nal_unit_type            =bit

    def getnal_unit_type(self):
        return self.nal_unit_type


    def  setrbsp(self,rbsp):
         self.rbsp                    =rbsp

    def getrbsp(self):
        return self.rbsp

    def add(self,dt):
        self.rbsp.append(dt)
    def get(self):
        return self.rbsp

    def __str__(self):
        return "nal basic information %d %d %d" %(self.forbidden_bit,self.nal_reference_bit,self.nal_unit_type)


