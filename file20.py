# class
class Pininterest:
    def images(self):
        print("this is used to download images for free")
a=Pininterest()  
a.images() 

# single inheritance
class Pininterest_shorts(Pininterest):
    def shorts(self):
        print("this features allows short videos of 30s and 60s")
a=Pininterest_shorts()
a.shorts()

# multilevel inheritance
class Pininterest_vlogs(Pininterest):
    def vlogs(self):
        print("this features allows vlogging option to fashion influencers , lifestyle preachers and others")
a=Pininterest_vlogs()
a.vlogs()

# multiple inheritance
class Pininterest_light:
    def light_version(self):
        print("this is a lighter version of Pininterest")
a=Pininterest_light()
a.light_version()



   