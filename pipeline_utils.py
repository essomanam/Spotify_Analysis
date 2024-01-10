import requests
from constantes import *
import json
from pymongo import MongoClient
import urllib.parse
import time

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2
ACCESS_TOKEN = None
transformed_data = []

def get_token():
    global ACCESS_TOKEN

    if ACCESS_TOKEN:
        return ACCESS_TOKEN

    data = {
        'grant_type': 'client_credentials',
        'client_id': API_CLIENT_ID,
        'client_secret': API_CLIENT_SECRET
    }
    
    try:
        response = requests.post("https://accounts.spotify.com/api/token", data=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        token_data = response.json()
        ACCESS_TOKEN = token_data.get('access_token')
        return ACCESS_TOKEN
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP call: {e}")
        print("Failed to fetch the access token")
        print("Response content:", response.content if response else None)
        return None

def http_call(url, data=None):
    global ACCESS_TOKEN

    params = {'url': url}
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'} if ACCESS_TOKEN else {}
    params.update(headers)

    if data:
        params.update(data)

    retries = 0
    MAX_RETRIES = 3  # You can adjust this based on your requirements

    while retries < MAX_RETRIES:
        try:
            response = requests.get(params['url'], headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return parse_json(response)
        except requests.exceptions.RequestException as e:
            print(f"Error during HTTP call: {e}")
            if response.status_code == 401 and retries < MAX_RETRIES:
                print("Retrying...")
                retries += 1
            else:
                return None

    print("Max retries exceeded. Exiting...")
    return None


def parse_json(response):
    try:
        return response.json()
    except ValueError:
        print("Error decoding JSON response")
        return None

def extract():
    for playlist in PLAYLIST_LIST:
        name, playlist_id = playlist['name'], playlist['id']
        with open(f'data/{name}_{playlist_id}.json', 'w', encoding='utf-8') as json_file:
            playlist_data = http_call(f'{API_URL}/v1/playlists/{playlist_id}')

            if playlist_data:
                track_ids = [track['track']['id'] for track in playlist_data.get('tracks', {}).get('items', [])]
                for track_id in track_ids:
                    track_data = http_call(f'{API_URL}/v1/tracks/{track_id}')

                    if track_data:
                        features = http_call(f'{API_URL}/v1/audio-features/{track_id}')

                        if features:
                            track_data["features"] = features
                            analysis = http_call(f'{API_URL}/v1/audio-analysis/{track_id}')

                            if analysis:
                                track_data["analysis"] = analysis
                                # Write each track_data as a separate JSON object
                                json.dump(track_data, json_file, ensure_ascii=False)
                                json_file.write('\n')  # Add a newline to separate JSON objects
                print(f"Les informations de la playlist {name} ont été sauvegardées dans '{name}_{playlist_id}.json'")

def transform():
    global transformed_data

    for playlist in PLAYLIST_LIST:
        name, playlist_id = playlist['name'], playlist['id']
        with open(f'data/{name}_{playlist_id}.json', 'r', encoding='utf-8') as json_file:
            for line in json_file:
                track_data = json.loads(line)
                transformed_data.append({
                    'playlist_name': name,
                    'track_name': track_data.get('name', ''),
                    'track_id': track_data.get('id', ''),
                    'popularity': track_data.get('popularity', ''),
                    'track_number' : track_data.get('track_number',''),
                    'album': {
                        'name': track_data.get('album', {}).get('name', ''),
                        'available_markets': track_data.get('album', {}).get('available_markets', ''),
                        'release_date': track_data.get('album', {}).get('release_date', ''),
                        'release_date_precision': track_data.get('album', {}).get('release_date_precision', ''),
                        'album_type':track_data.get('album',{}).get('album_type'),
                        'total_tracks': track_data.get('album',{}).get('total_tracks'),
                    },
                    'artists': [{
                        'name': artist.get('name', ''),
                        'followers': artist.get('followers', ''),
                        'genres': artist.get('genres', ''),
                        'popularity': artist.get('popularity',{}),
                    } for artist in track_data.get('artists', [])],
                    'audio_features': {
                        'acousticness': track_data.get('features', {}).get('acousticness', 0.0),
                        'danceability': track_data.get('features', {}).get('danceability', 0.0),
                        'energy': track_data.get('features', {}).get('energy', 0.0),
                        'instrumentalness': track_data.get('features', {}).get('instrumentalness', 0.0),
                        'loudness': track_data.get('features', {}).get('loudness', 0.0),
                        'liveness': track_data.get('features', {}).get('liveness', 0.0),
                        'tempo': track_data.get('features', {}).get('tempo', 0.0),
                        'mode': track_data.get('features', {}).get('mode', 0),
                        'speechiness': track_data.get('features', {}).get('speechiness', 0.0),
                        'valence': track_data.get('features', {}).get('valence', 0.0),
                        'durations_ms':track_data.get('features', {}).get('durations_ms',0),
                        'time_signature':track_data.get('features', {}).get('time_signature',0),
                        'key': track_data.get('features', {}).get('key',0),
                    },
                    'audio_analysis': {
                        'loudness': track_data.get('analysis', {}).get('loudness', 0.0),
                        'tempo': track_data.get('analysis', {}).get('tempo', 0.0),
                        'tempo_confidence': track_data.get('analysis', {}).get('tempo_confidence', 0.0),
                        'time_signature': track_data.get('analysis', {}).get('time_signature', 0),
                        'time_signature_confidence': track_data.get('analysis', {}).get('time_signature_confidence', 0.0),
                        'key': track_data.get('analysis', {}).get('key', 0),
                        'key_confidence': track_data.get('analysis', {}).get('key_confidence', 0.0),
                        'mode': track_data.get('analysis', {}).get('mode', 0),
                        'mode_confidence': track_data.get('analysis', {}).get('mode_confidence', 0.0),
                    }
                })

    print("Transformation complete.")

def load():
    global transformed_data

    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Insert transformed data into MongoDB
    collection.insert_many(transformed_data)

    # Close MongoDB connection
    client.close()