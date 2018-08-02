"""
  intruduction about mp4 file format,
  stream media  mp4 file,it contains a lot of
  box ,each box including a header,and body,like this:

  { [header,body],[header,body] ,[header,body],[header,body],[header,body]  }

  basic mp4 format just like that ,but maybe it's more complicated,

"""





from Mp4.mp4_parse import *

from Mp4.stream_file import  *


tools=mp4_parse("mp4_test.mp4")

tools.parse_ftyp_box()


tools.parse_moov_box()

print(tools)


# t=stream_file("mp4_test.mp4")
# print(t.readbytes(4))
# print(t.readbytes(4))
# print(t.current_pos())




