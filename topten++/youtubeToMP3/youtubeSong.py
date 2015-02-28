import pafy
import getpass

user = getpass.getuser()
url="https://www.youtube.com/watch?v=okCcL8daFAg&index=8&list=PLB71F7F05BAC030A2"
video=pafy.new(url)
audiostreams=video.audiostreams
bestAudio = video.getbestaudio()
bestAudio.download(filepath="/Users/" + str(user) +  "/Documents/topten++/youtubeToMP3/Songs")
