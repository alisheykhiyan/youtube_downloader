# youtube_downloader.py
from pytube import YouTube
link = input("Please enter the link:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
