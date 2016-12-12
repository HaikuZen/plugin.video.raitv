import urllib2
import json
import xbmc
from relinker import Relinker

class RaiPlay:
    baseUrl = "http://www.rai.tv"
    nothumb = "http://www.rai.it/cropgd/256x-/dl/components/img/imgPlaceholder.png"
    
    def getAllProgrammeList(self):
        url = "http://www.raiplay.it/dl/RaiTV/RaiPlayMobile/Prod/Config/programmiAZ-elenco.json"
        response = json.load(urllib2.urlopen(url))
        return response
        
    def getProgrammeList(self, url):
        xbmc.log("getProgrammeList url=" + url);
        response = json.load(urllib2.urlopen(url))
        xbmc.log("getProgrammeList Blocks="+str(response))
        return response["Blocks"]        
        
    def searchByIndex(self, index):
        xbmc.log("searchByIndex index=" + index)
        programmes = self.getAllProgrammeList()
        return programmes[index]
        
    def searchByName(self, name):
        xbmc.log("searchByName name=" + name);
        programmes = self.getAllProgrammeList()
        list =  []
        for index in programmes:
            for item in programmes[index]:
                if( name.upper() in item["name"].upper() ):
                    xbmc.log("searchByName found "+str(item))
                    list.append(item)
        return list   
        
    def getProgrammeBlocks(self, url):
        xbmc.log("getProgrammeBlocks "+self.baseUrl+url)
        response = json.load(urllib2.urlopen(self.baseUrl+url))
        videos = []
        for item in response["items"]:
            videos.append(self.getVideoUrl(item["pathID"]))
        return videos
        
    def getVideoUrl(self, url):
        xbmc.log("getVideoUrl "+self.baseUrl+url)
        response = json.load(urllib2.urlopen(self.baseUrl+url))
        url = response["video"]["contentUrl"]
        relinker = Relinker()
        url = relinker.getURL(url)
        xbmc.log("getVideoUrl relinked url "+url)
        return {"url": url, 
                "description": response["description"], 
                "image": response["images"]["landscape"],
                "name": response["name"],
                "subtitle": response["subtitle"]
                }
                
    def getImage(self, url):
        xbmc.log("getImage url "+url)
        #return urllib2.urlopen(url.replace("[RESOLUTION]","500x500")).read()
        return ""
       
        