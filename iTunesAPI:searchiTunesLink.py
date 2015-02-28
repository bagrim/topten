import urllib
artistname=raw_input("Enter name of artist:")
f = urllib.urlopen("https://itunes.apple.com/search?term="+artistname+"&entity=musicArtist")
temp=open("data.txt","w")
temp.write(str(f.read()))
temp.close()
temp=open("data.txt","r")
while temp:
	line=temp.readline()
	if line.find("http")>=0:
		n=line.find("http")
		output=""
		while(line[n]!='"'):
			output=output+line[n]
			n=n+1
		break
temp.close()
print output
temp=open("link.txt","w")
temp.write(output)






