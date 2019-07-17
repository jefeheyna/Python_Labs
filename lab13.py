class Song:
    def __init__(self,List_song):
        self.title=List_song[0]
        self.artist=List_song[1]
        self.album=List_song[2]
        self.length=int(List_song[3])

    def displayInfo(self):
        print("Title: ",self.title)
        print("Artist: ",self.artist)
        print("Album: ",self.album)
        print("Length(sec): ",self.length)
        print()

    def getLength(self):
        print(self.length)
        print()
        return self.length
    

    def getArtist(self):
        print(self.artist)
        print()
        return self.artist

class Playlist:
    def __init__(self,name,songlist):
        self.playlist=name
        self.songs=songlist
        num=0
        for song in self.songs:
            num+=1
        self.numsongs=num 
        
    def getName(self):
        print('Playlist: ',self.playlist)
        print()
        return self.playlist
    
    def getNumSongs(self):
        print('Number of songs in',self.playlist,'playlist: ',self.numsongs)
        print()
        return self.numsongs
    
    def getTotalTime(self):
        total=0
        for song in self.songs:
            total+=int(song[3])
        print('Total Time in',self.playlist,'playlist: ',total,'seconds')
        print()
        return total

    def getArtistSongs(self,artist):
        i=0
        print('Here are the songs with the artist',artist,'in the playlist',self.playlist,':')
        print()
        for song in self.songs:
            if song[1]==artist:
                artist_song=Song(song)
                artist_song.displayInfo()
                i+=1
        if i==0:
            print("There are no songs of this artist in this playlist.")
            print()
        
def main():
    playlist1=[]
    file1=open('playlist1.txt','r')
    playlist2=[]
    file2=open('playlist2.txt','r')
    playlist3=[]
    file3=open('playlist3.txt','r')
    for line in file1:
        line=line.strip('\n')
        value=line.split(', ')
        playlist1.append(value)
    for line in file2:
        line=line.strip('\n')
        value=line.split(', ')
        playlist2.append(value)
    for line in file3:
        line=line.strip('\n')
        value=line.split(', ')
        playlist3.append(value)

    song=Song(playlist1[0])
    song.displayInfo()
    song.getLength()
    song.getArtist()

    p1=Playlist('Beatles',playlist1)
    p1.getName()
    p1.getNumSongs()
    p1.getTotalTime()

    p2=Playlist('Random',playlist2)
    p2.getName()
    p2.getNumSongs()
    p2.getTotalTime()
    p2.getArtistSongs('The Beach Boys')
                  
      
main()
