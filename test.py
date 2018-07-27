

from Flv.flv import  *

from Flv.flv_parse import  *
import  binascii


flv_help=flv_parse("test.flv")
flv_help.parse_header()
flv_help.parse_tagN()

#
# a=bytearray(b'\x00\x04\xd1')
#
#
# #print(a.decode())
#
# xx=binascii.b2a_hex(a)
# print(int(xx,16))

#00 01 0A
#1
#10
#a=0#ff ff ff
#b=1
#c=10
#00 01 0a
#print(a*16*16*16+b*16*16+c)
#print()

#xx=format("{0:2}",str(hex(c)))
#print(xx)
#print("0{0}" % str(hex(a)) + str(hex(b)) + str(hex(c)))
#print(if len(str(hex(a)[2:]))==1  + str(hex(b)[2:]) + str(hex(c)[2:]))
# sum=int(str(hex(a)[2:]) + str(hex(b)[2:]) + str(hex(c)[2:]),16)
# print(sum)







