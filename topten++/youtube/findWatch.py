string = "watch"
infile=open("song1.txt","r") 
while infile:
    line=infile.readline()
    if line.find(string)>=0:
        n=line.find(string)
        s=""
        while(line[n]!=';'):
            s=s+line[n]
            n=n+1
        break    
s = "https://www.youtube.com/" + s 
print s