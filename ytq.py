from sub import *
from youtubesearchpython import *
import yt_dlp

def ytsq(link):
   tkid=link.split("/")[4].split("?")[0]

   videosSearch = VideosSearch(gettrack(tkid)[0], limit = 1)
   #print(gettrack(tkid)[0])
   print(videosSearch.result()['result'][0]['link'])
   id = videosSearch.result()['result'][0]['id']
   yhiu= videosSearch.result()['result'][0]['link']
   return id , yhiu

def ytdl(link):
   ytlink = [ ytsq(link)[1] ]
   ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
       }]
   }
   with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(ytlink)
    print('Downloaded.....!!')

def ytsn(name):
   videosSearch = VideosSearch(name, limit = 1)
   #print(name)
   print(videosSearch.result()['result'][0]['link'])
   id = videosSearch.result()['result'][0]['id']
   link= videosSearch.result()['result'][0]['link']
   return id , link

#ytdl("https://open.spotify.com/track/7uoFMmxln0GPXQ0AcCBXRq?si=yG2FixEhR_6lTNShrr0Mqg")