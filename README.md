# youtube-video-search-on-jupyter
This makes you use video search feture of Youtube Data API(v3) very easily on Jupyter notebook.

## Required
Python >= 3.4
Jupyter notebook >= 5

## Prerequisites 

- Youtube Data API(v3) require you to prepare API key.
To get the key, please read [this manual](https://developers.google.com/youtube/v3/getting-started).

- Please install Google APIs Client Library on Jupyter Notebook.

```
!pip install --upgrade google-api-python-client
```
## Specification of class
There are two classes to use this feature.

### YoutubeVideoSearch

### DisplayYoutubeVideo

*DisplayYoutubeVideo constructer needs YoutubeVideoSearch object.* 

e.g.)

```
yvs = YoutubeVideoSearch(key)
yvs.search('test')

dtv = DisplayYoutubeVideo(yvs)
```

|method|description|
| --- | --- |
|setAutoPlay <br> ( isAutoPlay : bool )| If isAutoPlay is True, video will start automatically without any clicks. Default is False. |
|setReplay <br> ( isReplay : bool )| If isReplay is True, a video will restart after it finishes. Default is False. |
|setStart <br> ( start : int )| If start is set, a video will start from the start time. |
|setEnd <br> ( end : int )| If end is set, a video will end at the end time. |
|play <br> ( playlist=[], multi=False )| This plays all movies you searched with YoutubeVideoSearch.search(). If you want to play 0th and 3th movie, please set playliset=[0,3]. If multi is True, movies are played simultaneously.If it's False, they are played one by one. |
|playFavorite <br> ( playlist=[], multi=False )| This plays all movies you appneded with YoutubeVideoSearch.appendFavorite(). Argument is the same as `play`.|
