import os
from pprint import pprint
import mutagen
import shutil
import random
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
old_directory = # Path of old directory 
new_directory = # Path to new directory


mp3Songs = []
m4aSongs = []

def removeBadCharactersMP3(value):
    deleteChars = '\\/:*?"<>|.'
    for char in deleteChars:
       value = value.replace(char, '')
    value = value.rstrip()
    return value

def removeBadCharactersMP4(value):
    deleteChars = '\\/:*?\'"<>|.[]'
    for char in deleteChars:
       value = value.replace(char, '')
    value = value.rstrip()
    return value

'''
Functions for testing
def mp3Function(root):
    print("These are MP3s: " + mp3Songs)
    info = mutagen.File(root + '\\' + mp3Songs)
    #print(info.pprint())
    artistName = info.get('TPE1')
    albumName = info.get('TALB')
    songTitle = info.get('TIT2')
    isinstance(artistName, str)
    print("Aritst: " + str(artistName))
    print("Album: " + str(albumName))
    print("Title: " + str(songTitle))
    print("-----")

def m4aFunction(root):
    print("These are M4As: " + m4aSongs)
    info = MP4(root + '\\' + filename)
    #print(info.pprint())
    artName = info['\xa9ART']
    albumName = info['\xa9alb']
    songTitle = info['\xa9nam']
    print("Aritst: " + str(artName))
    print("Album: " + str(albumName))
    print("Title: " + str(songTitle))
    print("-----")
'''

def newNameM4a(oldRoot):

    randomNumber = str(random.radint(0, 100))
    info = mutagen.File(oldRoot + '\\' + m4aSongs)
    oldMP4 = oldRoot + '\\' + m4aSongs
    artistName = str(info.get('\xa9ART'))
    artistName = removeBadCharactersMP4(artistName)
    albumName = str(info.get('\xa9alb'))
    albumName = removeBadCharactersMP4(albumName)
    songTitle = str(info.get('\xa9nam'))

    if len(songTitle) >= 200:
        songTitle = songTitle[:-100]
    songTitle = removeBadCharactersMP4(songTitle)
    #print(pprint(info))

    if artistName == "None":
        artistName = artistName + " " + randomNumber
    
    if albumName == "None":
        albumName = albumName + " " + randomNumber

    if songTitle == "None":
        songTitle = songTitle + " " + randomNumber


    songTitle = songTitle + '.m4a'

    print("Artist Title: " + artistName)
    print("Album Title: " + albumName)
    print("Song title: " + songTitle)
    print("m4a Song: " + m4aSongs)
    print("-----")


    for root, dirs, files in os.walk(new_directory):
        artistPath = os.path.join(new_directory, artistName)
        albumPath = os.path.join(artistPath, albumName)
        songPath = os.path.join(albumPath, songTitle)

        if not os.path.isdir(artistPath):
            os.mkdir(artistPath)            
            if not os.path.isdir(albumPath):
                print("made new album with song")
                os.mkdir(albumPath)                
                shutil.copyfile(oldMP4, songPath)                
            elif os.path.isdir(albumPath):
                print(albumName + " already an album folder")
                if not os.path.isfile(songPath):
                    shutil.copyfile(oldMP4, songPath)
                    print("made new song file")
                elif os.path.isfile(songPath):
                    print(songTitle + " already included in album")

        elif  os.path.isdir(artistPath):
            print(artistName + " already an artist folder")
            if not os.path.isdir(albumPath):
                print("made new album with song")
                
                os.mkdir(albumPath)                
                shutil.copyfile(oldMP4, songPath)                
            elif os.path.isdir(albumPath):
                print(albumName + " already an album folder")
                if not os.path.isfile(songPath):
                    shutil.copyfile(oldMP4, songPath)
                    print("made new song file")
                elif os.path.isfile(songPath):
                    print(songTitle + " already included in album")
        else:
            path = os.path.join(new_directory, str(artistName))
            os.mkdir(path)
            print("made directory for " + artistName)

def newNameMP3(oldRoot):

    randomNumber = str(random.radint(0, 100))
    info = mutagen.File(oldRoot + '\\' + mp3Songs)
    oldMP3 = oldRoot + '\\' + mp3Songs
    artistName = str(info.get('TPE1'))
    artistName = removeBadCharactersMP3(artistName)
    albumName = str(info.get('TALB'))
    albumName = removeBadCharactersMP3(albumName)
    songTitle = str(info.get('TIT2'))

    if len(songTitle) >= 200:
        songTitle = songTitle[:-100]
    songTitle = removeBadCharactersMP3(songTitle)

    if artistName == "None":
        artistName = artistName + " " + randomNumber
    
    if albumName == "None":
        albumName = albumName + " " + randomNumber

    if songTitle == "None":
        songTitle = songTitle + " " + randomNumber

    songTitle = songTitle + '.mp3'
    
    print("Album Title: " + albumName)
    print("Song title: " + songTitle)
    print("Mp3 Song: " + mp3Songs)
    print("-----")

    for root, dirs, files in os.walk(new_directory):
        artistPath = os.path.join(new_directory, artistName)
        albumPath = os.path.join(artistPath, albumName)
        songPath = os.path.join(albumPath, songTitle)

        if not os.path.isdir(artistPath):
            print("no artist folder for ~~" + artistName)
            os.mkdir(artistPath)            
            if not os.path.isdir(albumPath):
                print("made new album with song")
                
                os.mkdir(albumPath)                
                shutil.copyfile(oldMP3, songPath)                
            elif os.path.isdir(albumPath):
                os.chdir(albumPath)
                print(albumName + " already an album folder")
                if not os.path.isfile(songPath):
                    shutil.copyfile(oldMP3, songPath)
                    print("made new song file")
                elif os.path.isfile(songPath):
                    print(songTitle + " already included in album")

        elif os.path.isdir(artistPath):
            print(artistName + " already an artist folder")
            if not os.path.isdir(albumPath):
                print("made new album with song")
                
                os.mkdir(albumPath)                
                shutil.copyfile(oldMP3, songPath)                
            elif os.path.isdir(albumPath):
                print(albumName + " already an album folder")
                if not os.path.isfile(songPath):
                    shutil.copyfile(oldMP3, songPath)
                    print("made new song file")
                elif os.path.isfile(songPath):
                    print(songTitle + " already included in album")
        else:
            path = os.path.join(new_directory, str(artistName))
            os.mkdir(path)
            print("made directory for " + artistName)

for root, dirs, files, in os.walk(old_directory):
    
    for filename in files:        
        old_path = os.path.join( os.path.abspath(root), filename)
        audioFile = os.path.abspath(root)
        if len(filename) <= 8:        
            base, extension = os.path.splitext(filename)
            mp3Extension = 'mp3'
            m4aExtension = 'm4a'
            if mp3Extension in filename:
                #mp3Songs = filename
                #mp3Function(os.path.abspath(root)) 
                newNameMP3(os.path.abspath(root)) 


            if m4aExtension in filename:
                #m4aSongs = filename
                #m4aFunction(os.path.abspath(root))
                #print('These are M4As: '+ m4aSongs)
                newNameM4a(os.path.abspath(root))



    
