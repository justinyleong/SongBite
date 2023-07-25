from spotify import *
from downloader import *
import requests
import time
import vlc
from create_csv import *
from model import * 
from datetime import datetime, timedelta
from time import sleep


def main():
    link = input("Insert Spotify Link: ")
    playlist_id = link.replace("https://open.spotify.com/playlist/", "").split("?")[0]

    media_player = vlc.MediaPlayer()
    temp = 0

    # list of song names + artists, playlist name
    songs, playlist_name = getSongNames(playlist_id)
    # create list of video IDs from op yt api
    # yt_ids = []
    for i in songs:
        # play the prev one while searching for the new one for efficency
        res = requests.get("https://yt.lemnoslife.com/noKey/search?q=" + i)
        id = res.json()["items"][0]["id"]["videoId"]
        # print("https://www.youtube.com/watch?v=" + id)
        # downloading all songs
        # run analysis on songs and crop + play

        # downloading songs
        # print("downloading: " + id)
        title = download(id)
        # create csv
        create_csv(id, title)
        # find peaks
        print("🔎 Finding peaks . . .")
        peaks = find_song_peaks(id, title)

        sleep(5) # Or however long you expect it to take to open vlc
        temp2 = 0
        while media_player.is_playing():
            if temp != 0 and temp2 == 0:
                print("⏭️  In queue: " + title)
            sleep(1)
            temp2 += 1
        
        temp += 1

        media = vlc.Media(title + "_audio.mp4")
        print("🍕 Playing the tasty part: " + title)
        print("\n😋 😋 😋\n")
        # print(str(peaks[0]/1000))
        media.add_option('start-time=' + str(peaks[0]/1000))
        media.add_option('stop-time=' + str(peaks[0]/1000 + 10))
        media_player.set_media(media)
        media_player.play()
    
    sleep(5)
    while media_player.is_playing():
        sleep(1)
    

main()