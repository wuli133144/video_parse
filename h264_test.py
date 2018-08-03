

from Flv2H264.flv2h264 import *

from Flv2Aac.Flv2aac import *



tools=flv2h264("test.flv")

print(" ##################h265 size###################### ")
tools.flv2h264_def()

print(" ##################h265 size end###################### ")



toolsaac= flv2aac("test.flv")

toolsaac.flv2aac_def()