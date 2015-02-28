
import gdata.youtube
import gdata.youtube.service
import youtube_dl
import os
from subprocess import call

yt_service = gdata.youtube.service.YouTubeService()

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'relevance'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  temp=open("songdata.txt","w")
  temp.write(str(feed))
  temp.close()




songname=raw_input("Enter song to download:")
SearchAndPrint(songname) 

infile=open("songdata.txt","r")
while infile:
	line=infile.readline()
	if line.find("watch")>=0:
		n=line.find("watch")
		code=""
		count=1;
		while(line[n]!='&'):
			if count>=9 :
				code=code+line[n]
			n=n+1
			count=count+1
		break
infile.close()
os.remove("songdata.txt")
print code
command = "youtube-dl  "+code+" -x --audio-format mp3 -o %(title)s.(ext)s'"
call(command.split(), shell=False)