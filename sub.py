from youtubesearchpython import *
import yt_dlp
import json,csv,os
import requests
from refresh import *

token=retk()


def gettrack(track):
     global token
     URL = "https://api.spotify.com/v1/tracks/" + track + "?access_token=" + token
     r = requests.get(url = URL) 
     data = r.json()
     track = data['name']
     sample= data['preview_url']
     img = data['album']['images'][0]['url']
     return track, sample, img 


def getplay(playlistlink):
     playlist_id = playlistlink[34:].split('?')[0]
     URL = "https://api.spotify.com/v1/playlists/" + playlist_id  + "/tracks?access_token=" + token
     r = requests.get(url = URL) 
     total = r.json()['total']
     for i in range(total):
         Limit = 0
         if Limit == 100:
         
            print(i,r.json()['items'][i]["track"]["external_urls"]["spotify"])

    
 


getplay("https://open.spotify.com/playlist/6dBDprurUuVxaKlC2B2CJF?si=LZgnzMPJSlijLLlfRnd-5A")






#json_object = json.dumps(data)
     #with open("sample.json", "w+") as outfile:
      # outfile.write(json_object)



def rclone(name):
    rcl = "rclone --config './rclone.conf' copy '"+name+"' Mirror:/Music/ "
    os.system(rcl)
    print("Uploaded..!!")









def write(link,name):
  with open("links.csv","a+") as filec:
           cwrite = csv.writer(filec)
           cwrite.writerow([link,name])



def read():
   global cread
   filec = open("links.csv","r")
   cread=csv.reader(filec)
   return cread
 
def ytsq(link):
   tkid=link.split("/")[4].split("?")[0]

   videosSearch = VideosSearch(gettrack(tkid)[0], limit = 1)
   #print(gettrack(tkid)[0])
   #print(videosSearch.result()['result'][0]['link'])
   id = videosSearch.result()['result'][0]['id']
   yhiu= videosSearch.result()['result'][0]['link']
   return id , yhiu

def ytsn(query):
   videosSearch = VideosSearch(query, limit = 1)
   #print(videosSearch.result()['result'][0]['link'])
   id = videosSearch.result()['result'][0]['id']
   link = videosSearch.result()['result'][0]['link']
   title = videosSearch.result()['result'][0]['title']
   img = videosSearch.result()['result'][0]['thumbnails'][0]['url']
   return id , link , title , img 

def dytdl(link):
      ytdl = yt_dlp.YoutubeDL()
      ytdl.download(link)
      info=ytdl.extract_info(link)
      id = info['id']
      return id


def urlytdl(link):
      ydl_opts = {'format': 'mp4/240/best',
  }
      ytdl = yt_dlp.YoutubeDL(ydl_opts)
      info= ytdl.extract_info(link,download=False)
      return info['id'],info['url']


#print(urlytdl('https://www.pornhub.com/view_video.php?viewkey=ph6298b90bc6e55'))


def ytdl(link):
   ytlink = [ link ] 
   ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        }]
      }
   with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(ytlink)
