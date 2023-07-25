from pytube import YouTube
import os

def download(id):
    yt = YouTube('https://www.youtube.com/watch?v=' + id)
    yt.streams.first().download(filename='tempfile.mp4')

    # print(yt.streams.filter(only_audio=True))
    stream = yt.streams.get_by_itag(139)
    stream.download(filename='tempfile.mp4')

    print("⏬ Downloading: " + yt.title)
    if not os.path.exists("./audio_files/" + id + "_audio.mp4"):
        os.rename("tempfile.mp4", "./audio_files/" + id + "_audio.mp4")
        
    print("✅ Successfully downloaded")
    return yt.title