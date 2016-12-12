import urllib
import urllib2
import urlparse

class Relinker:
    __USERAGENT="Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    # Rai.tv android app
    # __USERAGENT = "Apache-HttpClient/UNAVAILABLE (java 1.4)"
    # Firefox 29 on Android
    # __USERAGENT = "Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0"
    # Firefox 29 on Windows 7
    # __USERAGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0"
    # Firefox 29 on Linux
    # __USERAGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0"
    # Raiplay android app
    #__USERAGENT = "Android 4.2.2 (smart) / RaiPlay 2.0.4 / WiFi"
    
    def __init__(self):
        opener = urllib2.build_opener()
        # Set User-Agent
        opener.addheaders = [('User-Agent', self.__USERAGENT)]
        urllib2.install_opener(opener)

    def getURL(self, url):
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(url)
        qs = urlparse.parse_qs(query)
    
        # output=20 url in body
        # output=23 HTTP 302 redirect
        # output=25 url and other parameters in body, space separated
        # output=44 XML (not well formatted) in body
        # output=47 json in body
        # pl=native,flash,silverlight
        # A stream will be returned depending on the UA (and pl parameter?)
        
        if "output" in qs:
            del(qs['output'])
        qs['output'] = "20"
        
        query = urllib.urlencode(qs, True)
        url = urlparse.urlunparse((scheme, netloc, path, params, query, fragment))
        
        print "Relinker URL: %s" % url
        
        #response = urllib2.urlopen(url)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', self.__USERAGENT)]
        response = opener.open(url)
        mediaUrl = response.read().strip()
        
        # Workaround to normalize URL if the relinker doesn't
        mediaUrl = urllib.quote(mediaUrl, safe="%/:=&?~#+!$,;'@()*[]")
        
        return mediaUrl

