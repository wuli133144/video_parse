

from Flv.flv_parse import  *
from Mp4.stream_file import *

import  struct

class flv2aac(object):
      def __init__(self,filepath):
          self.m_flv_parse=flv_parse(filepath)
          #self.file_help=stream_file("Temp.h264")
          self.m_aac_handle=None
          self.init()

      def init(self):

          try:
              self.m_aac_handle=stream_file("temp.aac")

          except FileExistsError:
              print("create h264file failed!")

      def flv2aac_def(self):

          self.m_flv_parse.parse_header()
          self.m_flv_parse.parse_tagN()
          aac=self.m_flv_parse.m_flv.getacc()
          print(len(aac))

          #self.m_h264_handle.writebytes(h264)

          print("##############start write data to h265file################")
          for i in range(len(aac)) :




                 data=str(aac[i][12:len(aac[i])-2])
                 sz = len(data)
                 format="%ds" %sz

                 pa=pack(format,data)

                 self.m_aac_handle.writebytes((pa))



                 pass

          print("##############start write data to h265file end ################")



      def __del__(self):
          pass





