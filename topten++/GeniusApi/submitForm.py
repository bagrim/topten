import urllib

f = urllib.urlopen("https://itunes.apple.com/search?term=metallica&entity=musicArtist")
print f.read()