import csv
import os





def pwrite(name,link):
  with open("playlist.csv","a+") as filec:
           cwrite = csv.writer(filec)
           cwrite.writerow([name,link])



def pread():
   global cread
   filec = open("playlist.csv","r")
   cread=csv.reader(filec)
   return cread






name = input("Enter The Name Of Your Playlist:")
link = input("Enter The Link Of Your Playlist:")



pwrite(name,link)