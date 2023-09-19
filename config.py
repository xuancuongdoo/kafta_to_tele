import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "google_api_key": os.environ.get("API_KEY"),
    "playlist_key": os.environ.get("PLAYLIST"),
}
