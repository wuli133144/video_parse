


FLV_HEADER_SIZE   =9
FLV_TAG_SIZE      =11
FLV_PRE_LEN       =4


FLV_FORMAT_SCRIPT =18
FLV_FORMAT_AUDEO  =8

FLV_FORMAT_VIDEO  =9

###########AMFTYPE#################################


AMF_TYPE_STRING    =0x02


AMF_TYPE_ARRAY     =0x08



#############audio#############################

def  get_audio_type(type):
     if isinstance(type,int) is False:
         return None

     if type ==10:
         return "AAC"
     elif type ==2:
         return "MP3"
     elif type == 0:
         return "Linear PCM，platform endian"
     elif type ==1:
         return "ADPCM"
     elif type == 3:
         return " Linear PCM，little endian"
     elif type ==4:
         return "Nellymoser 16-kHz mono"
     elif type ==5:
         return "Nellymoser 8-kHz mono"
     elif type == 6:
         return " Nellymoser"
     elif type ==7:
         return "G.711 A-law logarithmic PCM"
     elif type ==8:
         return "G.711 mu-law logarithmic PCM"
     elif type == 9:
         return "reserved"
     elif type ==14:
         return " MP3 8-Khz"
     elif type == 15:
         return " Device-specific sound"

     pass

def get_audio_samplerate(rate):
    if isinstance(type, int) is False:
        return None
    if rate == 0:
        return  5.5
    elif rate == 1:
        return 11
    elif rate == 2:
        return 22
    elif rate == 3:
        return 44


def get_audio_exactly(rate):
    if isinstance(type, int) is False:
        return None
    if rate == 0:
        return  8
    elif rate == 1:
        return 16

def get_audio_class(cs):
    if isinstance(type, int) is False:
        return None
    if cs == 0:
        return  "sndMono"
    elif cs == 1:
        return "sndStereo"

##############################################
def get_video_type(type):
    if isinstance(type, int) is False:
        return None

    if type == 1:
        return " keyframe （for AVC，a seekable frame）"
    elif type == 2:
        return " inter frame （for AVC，a nonseekable frame）"
    elif type == 3:
        return " disposable inter frame （H.263 only）"
    elif type == 4:
        return " generated keyframe （reserved for server use）"
    elif type == 5:
        return " video info/command frame"



def  get_amf_type_len(type):
    if isinstance(type, str) is False:
        return None

    if type =="Number":
        return 8
    elif type == "Boolean":
        return 1


