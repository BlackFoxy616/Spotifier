from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  



upload_file_list = ['Kanave Nee Naan - Kannum Kannum Kollaiyadithaal ｜ Dulquer S, Ritu V & Rakshan ｜ Masala Coffee [ZUcvKWegSGw].mp3', 'Selfie - Visual Glimpse - Badass Bossman Theme ｜ GV Prakash Kumar, Gautham Vasudev Menon, MathiMaran [AjRKjrcFeLc].mp3']


for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '13lQQ_BWpvYFPtjUG_Qs-DjQZRKvwU8m6'}]})
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.