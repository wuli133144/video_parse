




from Flv.flv_parse import  *
from Mp4.stream_file import *



class h264(object):
    def __init__(self,filepath):
        self.m_h264_handle = None
        self.init(filepath)


    def init(self,filepath):

        try:
            self.m_h264_handle = stream_file(filepath)

        except FileExistsError:
            print("create h264file failed!")


    def parse_h264(self):

        data=self.m_h264_handle.readbytes(1024)
        print(data)
        pass