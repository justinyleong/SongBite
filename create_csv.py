import requests
import pandas as pd
import numpy as np

def create_csv(id, title):
    url = "https://yt.lemnoslife.com/videos?part=mostReplayed&id="

    res = requests.get(url + id)

    heat_markers = res.json()["items"][0]["mostReplayed"]["heatMarkers"]

    timeRangeStartMillis = []
    heatMarkerIntensityScoreNormalized = []

    for i in heat_markers:
        timeRangeStartMillis.append(i["heatMarkerRenderer"]["timeRangeStartMillis"])
        heatMarkerIntensityScoreNormalized.append(i["heatMarkerRenderer"]["heatMarkerIntensityScoreNormalized"])
        # print(str(timeRangeStartMillis) + ", " + str(heatMarkerIntensityScoreNormalized))

    song_dict = {
        "time": timeRangeStartMillis,
        "heat_score": heatMarkerIntensityScoreNormalized
    }

    df = pd.DataFrame(song_dict)
    df.to_csv("./audio_files/" + id + ".csv", index=False)
    print("🪣  CSV created")

