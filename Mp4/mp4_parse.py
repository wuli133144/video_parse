
"""
mp4 support parse  maintain tools

"""


import  os
import  sys
import  math

from Mp4.stream_file import     *
from Mp4.ftypbox     import     *
from Mp4.define      import     *
from Mp4.freebox     import     *
from Mp4.mdatbox     import     *
from Mp4.moovbox     import     *
from Mp4.mvhd_box    import     *

from Mp4.track       import     *
from  Mp4.tkhdbox    import     *
from Mp4.edtsbox     import     *

from Mp4.DataBox import  *

from Mp4.elstbox import  *



import  binascii

#CURRENT_DIR=os.path.dirname()
VERSION="1.0.0"


class mp4_parse(stream_file):

    def __init__(self,filepath):
        self.m_boxs       =[]
        self.m_data       =None
        self.isstart      =0
        super().__init__(filepath)


    def parse_ftyp_box(self):


         #ftypbox_ojb=ftypbox()
         size=int(binascii.b2a_hex(self.readbytes(4)),16)
         data=self.readbytes(4)
         ty  ="%c%c%c%c" %(data[0],data[1],data[2],data[3])

         print(ty)
         print(size)
         if size ==0:
             print("mp4 file format error")
             return

         ftypbox_ojb = ftypbox(size,ty)
         major_branch=self.readbytes(4)
         major_branch="%c%c%c%c" %(major_branch[0],major_branch[1],major_branch[2],major_branch[3])

         minor_branch=int(binascii.b2a_hex(self.readbytes(4)), 16)


         compatible_branch=self.readbytes(4)

         compatible_branch = "%c%c%c%c" % (compatible_branch[0], compatible_branch[1], compatible_branch[2], compatible_branch[3])

         ftypbox_ojb.set_major_branch(major_branch)
         ftypbox_ojb.set_minor_version(minor_branch)
         ftypbox_ojb.set_compatible_brand(compatible_branch)

         print(ftypbox_ojb)

         self.m_boxs.append(ftypbox_ojb)
         self.isstart=1
         self.skip(8)
         self.parse_free_box()
         self.parse_mdat_box()

         pass

    def parse_free_box(self):
        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        ty = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        fbox=freebox(size,ty)
        #fbox.container.append([])
        self.m_boxs.append(fbox)


    def parse_mdat_box(self):
        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        ty = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("##########parse_mdat_box start ##########")
        data_container=self.readbytes(size-BOX_HEADER_SIZE)
        print("##########parse_mdat_box end ##########")
        mdabox=mdatbox(size,ty)
        mdabox.setdata(data_container)

        self.m_boxs.append(mdabox)


    def  parse_moov_box(self):
          if self.isstart ==0:
              print("please parse ftyp box firstly otherwise it's error")
              exit( -1)
              return
          # ftypbox_ojb=ftypbox()
          size = int(binascii.b2a_hex(self.readbytes(4)), 16)
          data = self.readbytes(4)
          ty = "%c%c%c%c" % (data[0], data[1], data[2], data[3])

          print(ty)
          print(size)

          mobox=moovbox(size,ty)
          ###########
          #todo
          ############
          #moovbox.add()
          self.parse_mvhd_box(mobox)
          self.parse_track(mobox)
          #######
          #self.parse_track(mobox)


    def parse_mvhd_box(self,movbox):
        if isinstance(movbox,moovbox) is False:
            print("please make sure moovbox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse mvlb############")
        print(size,type)
        print("###########parse mvlb end############")
        data_con=self.readbytes(size-BOX_HEADER_SIZE)
        mvhd=mvhdbox(size,type)
        mvhd.setdata(data_con)

        movbox.add(mvhd)

    def parse_track(self,movbox):
        if isinstance(movbox,moovbox) is False:
            print("please make sure moovbox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse parse_track############")
        print(size,type)
        print("###########parse parse_track end############")
        trabox=trackbox(size,type)
        ###parse tkhd box
        self.parse_tkhdbox(trabox)
        self.parse_edtsbox(trabox)
        self.parse_mdia(trabox)

        movbox.add(trabox)


        #data_con=self.readbytes(size-BOX_HEADER_SIZE)
        #mvhd=mvhdbox(size,type)
        #mvhd.setdata(data_con)
        #movbox.add(mvhd)

    def parse_mdia(self,trck):
        if isinstance(trck,trackbox) is False:
            print("please make sure trackbox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size,type)
        print("###########parse_mdia end############")
        dbox=databox(size,type)
        self.parse_mdhd(dbox)  ##dbox is mdia
        self.parse_hdlr(dbox)
        self.parse_minf(dbox)

    def parse_minf(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)

        self.parse_vmhd(dbox_minf)
        self.parse_dinf(dbox_minf)
        self.parse_stbl(dbox_minf)



    def parse_vmhd(self,dbox_minf):
        if isinstance(dbox_minf,databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size,type)
        print("###########parse_mdia end############")
        dbox_vmhd=databox(size,type)
        data=self.readbytes(size-BOX_HEADER_SIZE)
        dbox_vmhd.setdata(data)
        dbox_minf.add(dbox_vmhd)

        pass
    def parse_dinf(self,dbox_minf):

        if isinstance(dbox_minf, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox_minf.add(dbox_minf)

        self.parse_dref(dbox_minf)
        self.parse_url(dbox_minf)


        pass
    def parse_url(self,dbox_minf):
        if isinstance(dbox_minf, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_hdlr = databox(size, type)
        data = self.readbytes(size - BOX_HEADER_SIZE)
        dbox_hdlr.setdata(data)
        dbox_minf.add(dbox_hdlr)

    def parse_dref(self,dbox_minf):
        if isinstance(dbox_minf, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_hdlr = databox(size, type)
        # data = self.readbytes(size - BOX_HEADER_SIZE)
        # dbox_hdlr.setdata(data)
        dbox_minf.add(dbox_hdlr)

        pass

    def parse_stbl(self,dbox_minf):
        if isinstance(dbox_minf, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox_minf.add(dbox_minf)

        self.parse_stsd(dbox_minf)
        self.parse_stts(dbox_minf)
        self.parse_stss(dbox_minf)
        self.parse_stsc(dbox_minf)

        self.parse_stsz(dbox_minf)
        self.parse_stco(dbox_minf)


    def parse_stts(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass
    def parse_stss(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass
    def  parse_stsc(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass
    def parse_stsz(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass
    def parse_stco(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass

    def parse_stsd(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdia############")
        print(size, type)
        print("###########parse_mdia end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)

        self.parse_mp4v(dbox_minf)


    def parse_mp4v(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mp4v############")
        print(size, type)
        print("###########parse_mp4v end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        self.parse_esds(dbox_minf)
        self.parse_pasp(dbox_minf)
        pass


    def parse_esds(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_esds############")
        print(size, type)
        print("###########parse_esds end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass
    def parse_pasp(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_pasp############")
        print(size, type)
        print("###########parse_pasp end############")
        dbox_minf = databox(size, type)
        dbox.add(dbox_minf)
        pass

    def parse_hdlr(self,dbox):
        if isinstance(dbox, databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_hdlr############")
        print(size, type)
        print("###########parse_hdlr end############")
        dbox_hdlr = databox(size, type)
        data = self.readbytes(size - BOX_HEADER_SIZE)
        dbox_hdlr.setdata(data)
        dbox.add(dbox_hdlr)

    def parse_mdhd(self,dbox):
        if isinstance(dbox,databox) is False:
            print("please make sure databox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_mdhd############")
        print(size,type)
        print("###########parse_mdhd end############")
        dbox_mdhd=databox(size,type)
        data=self.readbytes(size-BOX_HEADER_SIZE)
        dbox_mdhd.setdata(data)
        dbox.add(dbox_mdhd)





    def parse_tkhdbox(self,trck):
        if isinstance(trck,trackbox) is False:
            print("please make sure trackbox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_tkhdbox############")
        print(size,type)
        print("###########parse_tkhdbox end############")
        tkhd=tkhdbox(size,type)
        data=self.readbytes(size-BOX_HEADER_SIZE)
        tkhd.setdata(data)

        trck.add(tkhd)

    def parse_edtsbox(self,trck):
        if isinstance(trck,trackbox) is False:
            print("please make sure trackbox type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
        # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_edtsbox############")
        print(size,type)
        print("###########parse_edtsbox end############")
        ###add edts box
        edts=edtsbox(size,type)
        trck.add(edts)

        self.parse_elstbox(edts)


    def parse_elstbox(self,edts):
        if isinstance(edts, edtsbox) is False:
            print("please make sure edts type ")
            return

        if self.isstart == 0:
            print("please parse ftyp box firstly otherwise it's error")
            exit(-1)
            return
            # ftypbox_ojb=ftypbox()
        size = int(binascii.b2a_hex(self.readbytes(4)), 16)
        data = self.readbytes(4)
        type = "%c%c%c%c" % (data[0], data[1], data[2], data[3])
        print("###########parse_elstbox############")
        print(size, type)
        print("###########parse_elstbox end############")
        ###add edts box
        elst = elstbox(size, type)
        data=self.readbytes(size-BOX_HEADER_SIZE)
        elst.setdata(data)
        edts.add(elst)



    def  __str__(self):
      return "mp4 parse tools file %s sized %d box number %d" % (self.getfilename(),self.getcapacity(),len(self.m_boxs))


