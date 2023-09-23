import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os
from dotenv import load_dotenv
import json

def date_input():
    while True:
        date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        try:
            global formatted_date
            formatted_date = datetime.strptime(date, r'%Y-%m-%d').strftime(r'%Y-%m-%d')
            if date == formatted_date:
                return date
            else:
                raise ValueError
        except ValueError:
            print("Invalid date format. Please try again.")

def main():
    song_list = []
    datetime_str = date_input()
    # print("Valid date:", datetime_str)
    url = "https://www.billboard.com/charts/hot-100"
    contents = requests.get(f"{url}/{datetime_str}")
    contents = contents.text
    soup = BeautifulSoup(contents, "html.parser")
    # search for the regex
    regex = re.compile(r'^c-title a-no-trucate')
    songs = soup.find_all("h3", class_=regex)
    #print(songs)
    for song in songs:
        song_list.append(song.getText().strip())
    print(song_list)
    # print(len(song_list))

    try:
        load_dotenv()
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        REDIRECT_URI = os.getenv("REDIRECT_URI")
        # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
        #                                         client_secret=CLIENT_SECRET,
        #                                         redirect_uri=REDIRECT_URI,
        #                                         scope="user-library-read",
        #                                         cache_path='./Day46-Spotify-Scrape-Billboard-Top-100/token.txt'))
        # results = sp.current_user_saved_tracks()
        # for idx, item in enumerate(results['items']):
        #     track = item['track']
        #     print(idx, track['artists'][0]['name'], " - ", track['name'])

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope="playlist-modify-private",
                                                show_dialog=True,
                                                cache_path='./Day46-Spotify-Scrape-Billboard-Top-100/token.txt'))
        # results = sp.current_user()
        # print(results['id'])
        #results = sp.me()
        #print(results['id'])

        date_year=datetime.strptime(formatted_date, r'%Y-%m-%d').strftime(r"%Y")
        print(date_year)
        song_uris=[]
        try:
            username = sp.current_user()["id"]
            playlist_name = f"{formatted_date} Billboard 100"
            global playlist
            playlist = sp.user_playlist_create(user=username, name=playlist_name, public=False)
            pprint(playlist)
            pprint(playlist['id'])
            
            for song in song_list:
                query = f"track:{song} year: {date_year}"
                # song_results = sp.search(q=query, limit=1,type='track')
                song_results = sp.search(q=query,type='track')
                # if song_results['tracks']['items'] exist
                if song_results['tracks']['items']:
                    track_uri = song_results['tracks']['items'][0]['uri']
                    song_uris.append(track_uri)
                else:
                    print(f"{song} does not exist in Spotify. Skipped.")
            pprint(song_results)

            sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

            # with open("./Day46-Spotify-Scrape-Billboard-Top-100/token.txt") as f:
            #     first_line = f.readline()
            #     first_line_json = json.loads(first_line)
            #     access_token = first_line_json['access_token']
            #     print(access_token)
            
            print(f"Playlist '{playlist_name}' created and {len(song_uris)} tracks added.")

        except Exception as e:
            print(f"{song} does not exist in Spotify. Skipped.")

    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()