from Flv.utils import *



class AMF_string(object):
    def __init__(self):
        self.amf_packet_type  =0x02
        self.amf_packet_length=len("@onMetaData")
        self.amf_packet_data  ="@onMetaData"

    def __repr__(self):
        print("amf_packet_type %d amf_packet_length %s"
              "amf_packet_data %s" %(self.amf_packet_type,self.amf_packet_length,self.amf_packet_data))


    def __str__(self):
        return ("amf_packet_type %d amf_packet_length %s"
              "amf_packet_data %s" % (self.amf_packet_type, self.amf_packet_length, self.amf_packet_data))