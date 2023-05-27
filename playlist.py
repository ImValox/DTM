import yt_dlp
import sys

def download_song(cleaned_artist, cleaned_title, download_folder):
    sys.stdout = open('output.txt', 'w')
    query = f"{cleaned_artist} {cleaned_title} Official Music"
    options = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_folder}/{cleaned_title} - {cleaned_artist}.%(ext)s',
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([f"ytsearch1:{query}"])
        sys.stdout.close()
        sys.stdout = sys.__stdout__