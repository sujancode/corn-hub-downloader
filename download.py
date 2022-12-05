import youtube_dl

ydl_opts_start = {
    'format': 'best',
    'playliststart:': 1,
    'playlistend': 4,
    'outtmpl': "./data/test.mp4",
    'nooverwrites': True,
    'no_warnings': False,
    'ignoreerrors': True
}

url = "https://www.pornhub.com/pornstar/eva-elfie"
with youtube_dl.YoutubeDL(ydl_opts_start) as ydl:
    ydl.download([url])
