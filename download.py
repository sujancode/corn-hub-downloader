import youtube_dl
import random
import string

while True:
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=7))

    ydl_opts_start = {
        'format': 'best',
        'playliststart:': 1,
        'playlistend': 4,
        'outtmpl': f"./data/{res}.mp4",
        'nooverwrites': True,
        'no_warnings': False,
        'ignoreerrors': True
    }

    url = "https://www.pornhub.com/pornstar/eva-elfie"
    with youtube_dl.YoutubeDL(ydl_opts_start) as ydl:
        ydl.download([url])
