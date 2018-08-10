from Flv.utils import *



class AMF_array(object):
    def __init__(self):
        self.amf_packet_array_type  =0x08
        self.amf_packet_array_count =0
        self.amf_packet_array_map   ={}


    def __int__(self,count,**iterms):
        self.amf_packet_array_type = 0x08
        self.amf_packet_array_count = count
        self.amf_packet_array_map = iterms
        pass
    def set_amf_packet_array_count(self,cnt):
        self.amf_packet_array_count=cnt

    def set_amf_packet_array_map(self,**iterms):
        self.amf_packet_array_map.setdefault(iterms.keys(),iterms.get(iterms.keys()))

    def __str__(self):

        return " amf_packet_array_type %d " \
               "amf_packet_array_count %d" \
               "amf_packet_array_map   %d" %(
                self.amf_packet_array_type,self.amf_packet_array_count,len(self.amf_packet_array_map))