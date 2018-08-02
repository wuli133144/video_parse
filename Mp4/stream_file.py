



class stream_file(object):


    def __init__(self,filepath):
        self.m_file_handle=None
        self.m_file_size  =0
        self.cur_pos      =-1
        self.file_name    =filepath
        self.init(filepath)

    def init(self,filepath):

        try:
            self.m_file_handle=open(filepath,'rb')
            self.m_file_size=self.m_file_handle.seek(0,2)
            self.m_file_handle.seek(0, 0)
        except FileExistsError :
            print("file  %s not found",filepath)

        pass


    def readbytes(self,bys):

        data= bytearray(self.m_file_handle.read(bys))
        self.cur_pos+=bys
        return data

    def current_pos(self):
        return self.cur_pos

    def getcapacity(self):
        return self.m_file_size

    def getfilename(self):
        return self.file_name

    def __str__(self):

        return " file %s size %d" %(self.file_name,self.m_file_size)


    def readbytes_pos(self,bys):
        self.m_file_handle.seek(self.cur_pos,0)
        data = bytearray(self.m_file_handle.read(bys))
        self.cur_pos += bys
        return data

    def skip(self,space):
        self.m_file_handle.seek(space, 1)

