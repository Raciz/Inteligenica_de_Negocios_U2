import os, sys

class files:
    Crimes = {}
    StopAndSearch = {}
    KML = []

    def __init__ (self):
        folders = ("CrimesUK_2011_2017","PoliceForce_KML","StopSearch_2011_2017")

        foldersCrimes = os.listdir(folders[0])

        for i in foldersCrimes:
            filesdir = folders[0]+"/"+i
            self.Crimes[i] = os.listdir(filesdir)

        for i in ["2011-","2012-","2013-","2014-","2015-","2016-","2017-"]:
            for j in ["01","02","03","04","05","06","07","08","08","10","11","12"]:
                print "i+j+": ",len(self.Crimes[i+j])



Files = files()
