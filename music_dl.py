import youtube_dl
from sys import argv

opts = {
    'format': 'bestaudio/best',
    'postprocessor': [{
        'key': 'FFmpegExtractAudio',
    }],
}

with youtube_dl.YoutubeDL(opts) as ydl:
        with open(argv[1], 'r') as music_file:
            ydl.download(music_file.readlines())
        print('All done!')
