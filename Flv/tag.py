



"""
 flv tag:
 type: scrip audio video
 header:11 bytes


"""
class flv_tag(object):

    def __init__(self):
        self.type             =None #1
        self.data_size        =None #2
        self.timestamp         =None  #时间戳  3

        self.timestamp_extend = None #1
        self.stream_id = None  # streamid 3
        self.data             =bytearray()  #数据

    def __init__(self,type):
        self.type = type  # 1
        self.data_size = None  # 2
        self.timestamp = None  # 时间戳  3

        self.timestamp_extend = None  # 1
        self.stream_id = None  # streamid 3
        self.data = bytearray()  # 数据

    def __str__(self):
         return " tag  type: %d  tag size:%d" \
                " timestamp:%d stream id:%d" %(self.type,self.timestamp,self.data_size,self.stream_id)
