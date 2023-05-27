import requests
import os
import playlist
from art import *
from colorama import init, Fore
import time

Deezertext = text2art("Deezer To MP3")
Madeby = "Made by Valox, check our website -> www.slash-mod.fr"
translation_dict = str.maketrans('', '', '/\\:*?"<>|')
download_folder=""
link = ""

def ask_download_folder():
    while True:
        download_folder = input(Fore.WHITE + "Please specify the download folder :" + Fore.RESET)
        download_folder = download_folder.strip()

        if os.path.isdir(download_folder):
            return download_folder
        else:
            print(Fore.RED + "The specified folder does not exist. Please try again." + Fore.RESET)

def ask_type():
    download_asktype = input(Fore.WHITE + "Would you like to download a Playlist or Album? (P/A)" + Fore.RESET)
    download_asktype = download_asktype.strip()
    if download_asktype == "P":
        download_type = "Playlist"
    elif download_asktype == "A":
        download_type = "Album"
    else:
        print(Fore.RED + "Invalid answer" + Fore.RESET)
        download_type = ask_type()
    return download_type

def remove_unicode_characters(text):
    encoded_text = text.encode("ascii", "ignore")
    cleaned_text = encoded_text.decode()
    return cleaned_text

def download_deezer_playlist(link, download_folder):
    try:
        response = requests.get(link)
        tracks = response.json()["tracks"]["data"]
    except:
        print("Playlist not found.")
        return

    for track in tracks:
        track_artist = track["artist"]["name"].translate(translation_dict)
        cleaned_artist = remove_unicode_characters(track_artist)

        track_title = track["title"].translate(translation_dict)
        cleaned_title = remove_unicode_characters(track_title)
        
        track_file = f"{download_folder}/{cleaned_title}.mp3"
        if os.path.isfile(track_file):
            print(f"{cleaned_title} - {cleaned_artist} |" + Fore.BLUE + " Already downloaded." + Fore.RESET)
            continue
        try:
            playlist.download_song(track_artist, cleaned_title, download_folder)
            print(f"{cleaned_title} - {cleaned_artist} |" + Fore.GREEN + " Downloaded successfully." + Fore.RESET)
        except:
            print(f"{cleaned_title} - {cleaned_artist} |" + Fore.RED + " Untraceable." + Fore.RESET)

download_deezer_playlist(link, download_folder)

while True:
    os.system('cls')
    print(Fore.MAGENTA + Deezertext + Fore.RESET)
    print(Fore.BLUE + Madeby + Fore.RESET)

    download_type = ask_type()
    if download_type is not None:
        print(Fore.WHITE + "Type selected :", download_type + Fore.RESET)
        if download_type == "Playlist":
            playlist_id = input(Fore.WHITE + "Playlist ID :" + Fore.RESET)
            link = f"https://api.deezer.com/playlist/{playlist_id}"
        elif download_type == "Album":
            music_id = input(Fore.WHITE + "Album ID:" + Fore.RESET)
            link = f"https://api.deezer.com/album/{music_id}"
    else:
        print(Fore.RED + "Error" + Fore.RESET)

    download_folder = ask_download_folder()
    if download_folder:
        print(Fore.WHITE + "Selected directory :", download_folder + Fore.RESET)
    else:
        print(Fore.RED + "No directory selected " + Fore.RESET)
    download_deezer_playlist(link, download_folder)
    time.sleep(3)
    os.system('cls')
    response = input("Do you want to download anything else? (Yes/No)")
    if response.lower() != "yes" and response.lower() != "y":
        break