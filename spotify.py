import requests
import base64
# from secrets import *
import json

clientId = "11d5b22840294e74a37fb7a3e1cdca49"
clientSecret = "8e46a6fae0e448239bf2fb510f341dae"

def getSongNames(playlistId):
  url = 'https://accounts.spotify.com/api/token'
  headers = {}
  data = {}

  message =   f"{clientId}:{clientSecret}"
  messageBytes = message.encode('ascii')
  base64Bytes = base64.b64encode(messageBytes)
  base64Message = base64Bytes.decode('ascii')

  headers['Authorization'] = f"Basic {base64Message}"
  data['grant_type'] = "client_credentials"

  r = requests.post(url, headers=headers, data=data)

  token = r.json()['access_token']

  playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
  headers = {"Authorization": "Bearer " + token}

  res = requests.get(url=playlistUrl, headers=headers)

  tracks = json.loads(json.dumps(res.json(), indent=2))

  playlist_name = tracks['name']
  songs = []
  for i in tracks["tracks"]["items"]:
    artists = ""
    for j in i["track"]["artists"]:
      artists = artists + " " + j["name"]
    songs.append(i["track"]["name"] + " " + artists)
  
  return songs, playlist_name

playlistId = "5djnwrzJMMlFq9cHAvH2xo"
getSongNames(playlistId)