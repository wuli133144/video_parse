


class flv_header(object):
    def __init__(self,m,v,at,vt):
        self.mark=m
        self.version=v
        self.audio_type=at
        self.video_type=vt

    def __init__(self):
        self.mark = ""
        self.version =0
        self.audio_type = 0
        self.video_type = 0


    def __repr__(self):
        print(self.mark+"version:"+str(self.version)+" audio type:"+str(self.audio_type)+" video type:"+ str(self.video_type))

    def __str__(self):
        return "tag: "+self.mark+"version:"+str(self.version)+" audio type:"+str(self.audio_type)+" video type:"+ str(self.video_type)