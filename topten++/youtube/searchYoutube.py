import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'viewCount'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  text_file = open("song" + str(1) + ".txt", "w")
  text_file.write(str(feed))
  text_file.close()

SearchAndPrint("Highway to hell") 