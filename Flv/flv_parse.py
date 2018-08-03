
"""
sunlands

"""

from Flv.flv import *
from struct import  *
from Flv.utils import *
from Flv.tag import *
import string

import  binascii

class flv_parse(object):

    def __init__(self,filepath):
        self.m_file=filepath
        self.m_flv = flv()
        self.m_data=None
        self.m_size=0
        self.cur=0

        self.init()

    def init(self):
        if isinstance(self.m_file,str) is False:
            return  None
        try:
             with open(self.m_file,"rb") as f:
                  self.m_data=bytearray(f.read())
                  self.m_size=(f.tell())
                  pass
        except  (FileExistsError) :
            print("flv file not found!")

    def getsize(self):
        return self.m_size

    def parse_header(self):
        header=None
        if self.m_size == 0:
            return None
        #print(self.m_data)
        for i in range(3):
            self.m_flv.head.mark+="{0}".format(hex(self.m_data[i]))

        self.m_flv.head.version=self.m_data[3]
        #0000 0110
        self.m_flv.head.video_type=(self.m_data[4]) & 0x4 #0000 0100
        self.m_flv.head.audio_type = (self.m_data[4]) & 0x1  # 0000 0001 &0000 0001

        #print(self.m_flv.head)
        self.cur+=FLV_HEADER_SIZE

        pass

    """
     tag format like this
     [tag type :1bytes][data sie :3 bytes][timestam:3 bytes] [timestamp_extent 1bytes ] [stream id :3 bytes]=11
         
  
    """
    def  parse_tagN(self):
        tag=-1
        i=FLV_HEADER_SIZE  #flv header size


        while i <=self.m_size:

             i += FLV_PRE_LEN
             self.cur=i
             if i >=self.m_size:
                 break


             #print(i)
             try:
                 if   self.m_data[i] == FLV_FORMAT_SCRIPT:
                      tag+=1
                      print("flv_script:", tag)
                     ################################################################

                      t_size=0
                      i=i+1 #jump over type
                      t_size=int(binascii.b2a_hex(self.m_data[i:i+3]),16)

                     ####################################################################

                      i+=3
                      t_tmstamp=0
                      """
                     calculate timestamp
                      """
                      t_tmstamp = int(binascii.b2a_hex(self.m_data[i:i+3]),16)


                      """
                       jump timestamp_extent 1 bytes
                       
                      """
                      i+=1

                      """
                           calculate t_stream_id
                      """
                      i+=3

                      t_stream_id = int(binascii.b2a_hex(self.m_data[i:i+3]),16)

                      i+=3     #now offset data
                      t_data=""

                      """
                       calculate t_data
                      """
                      # for j in range(i,i+t_size):
                      #      t_data+=str(self.m_data[j])

                      t_data=str(self.m_data[i:i+t_size])

                      i+=t_size
                      tg=flv_tag()
                      tg.type=FLV_FORMAT_SCRIPT
                      tg.data_size=t_size
                      tg.timestam=t_tmstamp
                      tg.stream_id=t_stream_id
                      tg.data=t_data
                      self.m_flv.tagN.append(tg)

                      print("<all script>tg.type:%d %d %d %d i=%d " % (tg.type ,tg.data_size,tg.timestam,tg.stream_id,i))


                 elif self.m_data[i] == FLV_FORMAT_AUDEO:
                    tag += 1
                    print("flv_audio", tag)
                    i=i+1
                    t_size =int(binascii.b2a_hex(self.m_data[i:i+3]),16)

                    i += 3
                    t_tmstamp = int(binascii.b2a_hex(self.m_data[i:i+3]),16)

                    i += 3
                    #jump tm_extent
                    i+=1



                    t_stream_id= int(binascii.b2a_hex(self.m_data[i:i+3]),16)

                    i += 3  # now offset data
                    t_data = ""

                    """
                         calculate t_data
                    """
                    stream_type=(self.m_data[i] &0xf0)>>4

                    i=i+1
                    t_data           = str(self.m_data[i:i + t_size])
                    i                += t_size-1
                    tg               = flv_tag()
                    tg.type          = FLV_FORMAT_AUDEO
                    tg.data_size     = t_size
                    tg.timestam      = t_tmstamp
                    tg.stream_id     = t_stream_id

                    tg.stream_type   =get_audio_type(stream_type)

                    tg.data          = t_data
                    self.m_flv.tagN.append(tg)
                    self.m_flv.addaac(t_data)

                    print("<all audio>tg.type:%d %d %d %d  %s i=%d" % (tg.type, tg.data_size, tg.timestam, tg.stream_id,tg.stream_type,i))

                 elif self.m_data[i] == FLV_FORMAT_VIDEO:
                    tag += 1
                    print("flv_video", tag)
                    i=i+1
                    t_size = int(binascii.b2a_hex(self.m_data[i:i+3]),16)


                    i += 3
                    t_tmstamp =int(binascii.b2a_hex(self.m_data[i:i+3]),16)
                    """
                    calculate timestamp
                    """
                    i+=3
                    """
                     jump over timestamp_extent
                    """
                    i+=1
                    t_stream_id = int(binascii.b2a_hex(self.m_data[i:i+3]),16)

                    i+=3
                    t_data = ""

                    """
                         calculate t_data
                         
                    """
                    stream_type = (self.m_data[i] & 0xf0) >> 4

                    i = i + 1


                    t_data = str(self.m_data[i:i + t_size])
                    i += t_size-1
                    tg = flv_tag()
                    tg.type = FLV_FORMAT_VIDEO
                    tg.data_size = t_size
                    tg.timestam = t_tmstamp
                    tg.stream_id = t_stream_id
                    tg.data = t_data
                    tg.stream_type=get_video_type(stream_type)
                    self.m_flv.tagN.append(tg)

                    self.m_flv.addh264(t_data)
                    print("<all audio>tg.type:%d %d %d %d  %s i=%d" % (tg.type, tg.data_size, tg.timestam, tg.stream_id,tg.stream_type,i))

                 #i+=FLV_PRE_LEN

             except IndexError :
                 print("out range of array")


        print("<end parse stream resource> %d" %(self.cur))








