# youtube-video-search-on-jupyter
This makes you use video search feature of Youtube Data API(v3) very easily on Jupyter notebook.  
  
![image](https://github.com/simplestreet/youtube-video-search-on-jupyter/blob/master/image/top.gif)

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

## How to import

On jupyter notebook, import youtube-video-search.py file with `run` command.

```
%run D:\\source\\youtube-video-search-on-jupyter\\youtube-video-search.py
```

## Specification of class
There are two classes to use this feature.

### YoutubeVideoSearch

*YoutubeVideoSearch needs API key.* 

e.g.)

```
API_KEY = "Repalace_With_Your_Api_Key"

yvs = YoutubeVideoSearch(API_KEY)

try:
    yvs.search('mob psycho 2')
except HttpError as e:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
    raise e
else:
    print('Search succeded!')
```

|method|argument|description|e.g.|
| --- | --- | --- | --- |
|search| <p>options : str or dictionary</p><p> dictionary can be specified "q, maxResults, order"</p><p>(*1</p> | search videos with options. | search('Ariana Grande') 　<br> search( { <br>  'q' : 'Ariana Grande', <br>  'maxResults' : '3', <br>  'order' : 'viewCount' <br>} )|
|showResults| - | show the result of your search. ||
|getSearchCount| - | show the number of the result. ||
|next| - | get the next page of the result. ||
|appendFavorite| index : int | store element specified by index. ||
|deleteFavorite| index : int | delete the element you appended by index. ||
|showFavorite| - | show all elements you appended. ||
|clearFavorite| - | clear all elements you appended. ||

<p>(*1 Please see `Search:list parameter` of YouTube Data API (v3) document.</p>

### DisplayYoutubeVideo

*DisplayYoutubeVideo needs YoutubeVideoSearch object.* 

e.g.)

```
yvs = YoutubeVideoSearch(key)
yvs.search('test')

dtv = DisplayYoutubeVideo(yvs)
```

|method|argument|description|
| --- | --- | --- |
|setAutoPlay| isAutoPlay : bool | If isAutoPlay is True, video will start automatically without any clicks. Default is False. |
|setReplay| isReplay : bool | If isReplay is True, a video will restart after it finishes. Default is False. |
|setStart| start : int | If start is set, a video will start from the start time. |
|setEnd| end : int | If end is set, a video will end at the end time. |
|play| playlist=[], multi=False | This plays all movies you searched with YoutubeVideoSearch.search(). If you want to play 0th and 3th movie, please set playliset=[0,3]. If multi is True, movies are played simultaneously.If it's False, they are played one by one. |
|playFavorite| playlist=[], multi=False | This plays all movies you appneded with YoutubeVideoSearch.appendFavorite(). Argument is the same as `play`.|
