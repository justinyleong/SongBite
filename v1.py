from spotify import *
from downloader import *
import requests
import time
import vlc
from create_csv import *
from model import * 
from time import sleep


def main(playlist_id):
    # list of song names + artists, playlist name
    songs, playlist_name = getSongNames(playlist_id)
    # create list of video IDs from op yt api
    yt_ids = []
    for i in songs:
        # play the prev one while searching for the new one for efficency
        res = requests.get("https://yt.lemnoslife.com/noKey/search?q=" + i)
        id = res.json()["items"][0]["id"]["videoId"]
        yt_ids.append(id)
        print("https://www.youtube.com/watch?v=" + id)
        time.sleep(0.5)

    # downloading all songs
    # run analysis on songs and crop + play
    for i in yt_ids:
        # downloading songs
        print("downloading: " + i)
        title = download(i)
        # create csv
        create_csv(i, title)
        # find peaks
        print("finding peaks . . .")
        peaks = find_song_peaks(i, title)
        # play songs with the peaks

        # should i create a new media player each time?
        media_player = vlc.MediaPlayer()

        media = vlc.Media(title + ".mp4")
        media.add_option('start-time=' + str(peaks[0]/1000))
        media.add_option('stop-time=' + str(peaks[0]/1000 + 20))
        media_player.set_media(media)
        media_player.play()

        # or move all the prep for the next song into this place so its optimized
        # sleep for the time you want the audio to play
        # sleep(20)

        sleep(5) # Or however long you expect it to take to open vlc
        while media_player.is_playing():
            sleep(1)


    
    

main("26yiQKcYFuHWLiBZNvgqJW")