




from Flv.flv_parse import  *
from Mp4.stream_file import *
from h264_tools.h264_define import *
from h264_tools.nal import         *
import  os


class h264(stream_file):

    def __init__(self,filepath):
        super().__init__(filepath)
        self.nals = []





    def parse_h264(self):

        data=self.readbytes(1024)
        print(data)
        pass

    def findstartcode4bits(self):
        startcode=self.readbytes(4)
        if startcode[0:] == bytearray([0x00,0x00,0x00,0x01]):
            return True,startcode
            pass

        return False,startcode
    def findstartcode3bits(self):
        startcode = self.readbytes(3)
        if startcode[0:] == bytearray([0x00,0x00,0x01]):
            return True,startcode
            pass

        return False ,startcode

    def  getnalutype(self,naluheader):

        if naluheader & 0x1f == 0x05:
            print("IDR")
            return NALU_TYPE_IDR
            pass
        elif naluheader & 0x1f == 0x06:
            print("SEI")
            return NALU_TYPE_SEI
            pass
        elif naluheader & 0x1f == 0x07:
            print("SPS")
            return NALU_TYPE_SPS
            pass
        elif naluheader & 0x1f == 0x08:
            print("PPS")
            return  NALU_TYPE_PPS
            pass
        elif naluheader & 0x1f == 0x09:
            print("AUD")
            return  NALU_TYPE_AUD
            pass
        elif naluheader & 0x1f == 0x0a:
            print("EOSEQ")
            return NALU_TYPE_EOSEQ
            pass
        elif naluheader & 0x1f == 0x0b:
            print("EOSTREAM")
            return NALU_TYPE_EOSTREAM
            pass
        elif naluheader& 0x1f == 0x0c:
            print("FILL")
            return NALU_TYPE_FILL
            pass
        elif naluheader & 0x1f == 0x01:
            print("SLICE")
            return NALU_TYPE_SLICE
            pass
        elif naluheader & 0x1f == 0x02:
            print("DPA")
            return NALU_TYPE_DPA
            pass
        elif naluheader & 0x1f == 0x03:
            print("DPB")
            return NALU_TYPE_DPB
            pass
        elif naluheader & 0x1f == 0x04:
            print("DPC")
            return NALU_TYPE_DPC
            pass
        else:
            print("nalu type error!")
            return -1

    def getpriority(self,naluheader):
        if ((naluheader & 0x60) >> 5)==0:

            return NALU_PRIORITY_DISPOSABLE
            pass
        elif ((naluheader & 0x60) >> 5)==1:

            return NALU_PRIRITY_LOW
            pass
        elif ((naluheader & 0x60) >> 5)==2:

            return NALU_PRIORITY_HIGH
            pass
        elif ((naluheader & 0x60) >> 5)==3:

            return NALU_PRIORITY_HIGHEST
            pass

        pass
    def h264_decode_nal(self):


            bRet,startcode=self.findstartcode3bits()

            if bRet == True:

                naluheader=(self.readdatas(1))

                priority=self.getpriority(naluheader[0])
                type    =self.getnalutype(naluheader[0])
                nalu    = nal(0,priority,type,startcode)

                data =self.readdatas(BUFFER_SIZE)
                i=0

                while data!=None:
                    while i < BUFFER_SIZE:

                        if  not (data[i] ==0 and data[i+1] == 0 and data[i+2]==1) :
                            if data[i] ==0 and data[i+1] == 0 and data[i+2] == 3:
                                data[i+2:]=data[i+3:]


                            nalu.add(data[i])
                            i += 1
                        elif data[i] ==0 and data[i+1] == 0 and data[i+2]==1 :
                            priority = self.getpriority(data[i+3])
                            type = self.getnalutype(data[i+3])
                            nalu = nal(0, priority, type, startcode)
                            i+=1
                            pass
                        if i >=BUFFER_SIZE:
                            print("xxxxxxxxxxxxx")
                        print(i)


                    print(nalu)
                    del data
                    data = self.readdatas(BUFFER_SIZE)















            else:
                bRet = self.findstartcode4bits()
                if bRet is True:
                    pass
                else:
                    print("h264 data format error!")
                    return






    def __str__(self):
        return "h264 decode nal unit"