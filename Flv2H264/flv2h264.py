

from Flv.flv_parse import  *
from Mp4.stream_file import *

import  struct

class flv2h264(object):
      def __init__(self,filepath):
          self.m_flv_parse=flv_parse(filepath)
          #self.file_help=stream_file("Temp.h264")
          self.m_h264_handle=None
          self.init()

      def init(self):

          try:
              self.m_h264_handle=stream_file("temp.h264")

          except FileExistsError:
              print("create h264file failed!")

      def flv2h264_def(self):

          self.m_flv_parse.parse_header()
          self.m_flv_parse.parse_tagN()
          h264=self.m_flv_parse.m_flv.geth264()
          print(len(h264))

          #self.m_h264_handle.writebytes(h264)

          print("##############start write data to h265file################")
          for i in range(len(h264)) :




                 data=str(h264[i][12:len(h264[i])-2])
                 sz = len(data)
                 format="%ds" %sz

                 pa=pack(format,data)

                 self.m_h264_handle.writebytes((pa))



                 pass

          print("##############start write data to h265file end ################")



      def __del__(self):
          pass





