#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from IPython.display import YouTubeVideo,Image

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class YoutubeVideoSearch:
    __searchResults = {}
    __searchResultList = []
    __nextPageToken=''
    __currentOptions={}
    __favorites=[]

    def __init__(self, key):
        if not key:
            raise ValueError("YoutubeApi requires developer key")
        self.__youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
            developerKey=key)

    def appendFavorite(self, index):
        self.__favorites.append(self.__searchResultList[index])

    def deleteFavorite(self, index):
        del self.__favorites[index]

    def showFavorite(self):
        self.showResults(favorite=True)

    def clearFavorite(self):
        self.__favorites.clear()

    def getFavorite(self):
        return self.__favorites

    def getSearchResultList(self):
        return self.__searchResultList

    def getSearchCount(self):
        print(len(self.__searchResultList))

    def showResults(self,favorite=False):
        if not self.__searchResultList:
            print('search result is empty')
            return
        if not favorite:
            search_results = self.__searchResultList
        else:
            search_results = self.__favorites
        i = 0
        for search_result in search_results:
            print('[%d]' % i)
            print('videoId : %s' % search_result["videoId"])
            print('channelId : %s' % search_result["channelId"])
            print('channelTitle : %s' % search_result["channelTitle"])
            print('liveBroadcastContent : %s' % search_result["liveBroadcastContent"])
            print('title : %s' % search_result["title"])
            print('description : %s' % search_result["description"])
            print('thumbnail_default: %s' % search_result["thumbnail_default"])
            print('thumbnail_medium : %s' % search_result["thumbnail_medium"])
            print('thumbnail_high   : %s' % search_result["thumbnail_high"])
            print('publishedAt   : %s' % search_result["publishedAt"])
            try:
                __IPYTHON__
            except NameError:
                pass
            else:
                display(Image(search_result["thumbnail_medium"]))
            print("\n")
            i+=1

    def next(self):
        options = self.__currentOptions
        options.update({'pageToken' : self.__nextPageToken})
        print(options)
        self.search(options)

    def search(self,options):
        defaultSearchType = {
                               'part' : 'id,snippet',
                               'type' : 'video'
        }
        if type(options) is str:
            options = {'q': options}
        search_response = self.__youtube.search().list(
          q=options['q'] if 'q' in options else None,
          part=defaultSearchType['part'],
          type=defaultSearchType['type'],
          pageToken=options['pageToken'] if 'pageToken' in options else None,
          maxResults=options['maxResults'] if 'maxResults' in options else None,
          order=options['order'] if 'order' in options else None
        ).execute()

        self.__currentOptions = options
        if 'nextPageToken' in search_response:
            self.__nextPageToken = search_response['nextPageToken']

        self.__searchResults=search_response.get("items", [])
        self.__searchResultList.clear()
        for search_result in self.__searchResults:
            if search_result["id"]["kind"] == 'youtube#video':
                tmp = {}
                tmp['videoId'] = search_result["id"]["videoId"]
                tmp['channelId'] = search_result["snippet"]["channelId"]
                tmp['channelTitle'] = search_result["snippet"]["channelTitle"]
                tmp['liveBroadcastContent'] = search_result["snippet"]["liveBroadcastContent"]
                tmp['title'] = search_result["snippet"]["title"]
                tmp['description'] = search_result["snippet"]["description"]
                tmp['thumbnail_default'] = search_result["snippet"]["thumbnails"]["default"]["url"]
                tmp['thumbnail_medium'] = search_result["snippet"]["thumbnails"]["medium"]["url"]
                tmp['thumbnail_high'] = search_result["snippet"]["thumbnails"]["high"]["url"]
                tmp['publishedAt'] = search_result["snippet"]["publishedAt"]
                self.__searchResultList.append(tmp)

class DisplayYoutubeVideo:

    def __init__(self, obj):
        if type(obj) is not YoutubeVideoSearch:
            raise ValueError("DisplayYoutubeVideo needs YoutubeVideoSearch instance!!")
        self.refreshConfig()
        self.__youtube = obj
        self.__start = 0
        self.__end = 0
        self.__isAutoPlay = False
        self.__isReplay = False

    def refreshConfig(self):
        self.__start = 0
        self.__end = 0
        self.__isAutoPlay = False
        self.__isReplay = False

    def setAutoPlay(self, isAutoPlay: bool):
        if type(isAutoPlay) is not bool:
            raise ValueError("setAutoPlay argument must be boolean type !!")
        self.__isAutoPlay = isAutoPlay

    def setReplay(self, isReplay: bool):
        if type(isReplay) is not bool:
            raise ValueError("setReplay argument must be boolean type !!")
        self.__isReplay = isReplay

    def setStart(self, start: int):
        if type(start) is not int:
            raise ValueError("setStart argument must be int type !!")
        self.__start = start

    def setEnd(self, end: int):
        if type(end) is not int:
            raise ValueError("setEnd argument must be int type !!")
        self.__end = end

    def playFavorite(self, playlist=[], multi=False):
        self.play(playlist=playlist, multi=multi, favorite=True)

    def play(self, playlist=[], multi=False, favorite=False):
        vids = []
        if not favorite:
            search_results = self.__youtube.getSearchResultList()
        else:
            search_results = self.__youtube.getFavorite()

        for search_result in search_results:
            vids.append("%s" % (search_result["videoId"]))
        if playlist != []:
            if len(vids) > max(playlist):
                vids = [vids[i] for i in playlist]
            else:
                raise IndexError("playlist argument is not correct")
        
        if multi == False and len(vids) >= 2:
            tvid=YouTubeVideo(vids[0],
                        autoplay=1 if self.__isAutoPlay == True else 0 ,
                        loop=1 if self.__isReplay == True else 0 ,
                        playlist=','.join(vids[1:]),
                        width='640',
                        height='360',
                        start=self.__start,
                        end=self.__end)
            display(tvid)
        else:
            for vid in vids:
                tvid=YouTubeVideo(vid,
                          autoplay=1 if self.__isAutoPlay == True else 0 ,
                          loop=1 if self.__isReplay == True else 0 ,
                          playlist=vid if self.__isReplay == True else '',
                          width='640',
                          height='360',
                          start=self.__start,
                          end=self.__end)
                display(tvid)