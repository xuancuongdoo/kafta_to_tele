#!/usr/bin/env python

import logging
import sys
import requests
import json
from config import config
from pprint import pformat


def fetch_playlist_items_page(google_api_key, playlist_id, page_token=None):
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": google_api_key,
            "playlistId": playlist_id,
            "part": "contentDetails",
            "pageToken": page_token
        })
    payload = json.loads(response.text)

    logging.debug("GOT %s", payload)
    return payload


def fetch_videos_pages(google_api_key, video_id, page_token=None):

    response = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={
            "key": google_api_key,
            "id": video_id,
            "part": "snippet, statistics",
            "pageToken": page_token
        })
    payload = json.loads(response.text)

    logging.debug("GOT %s", payload)
    return payload


def fetch_playlist_items(google_api_key, playlist_id, page_token=None):

    payload = fetch_playlist_items_page(
        google_api_key, playlist_id, page_token)

    yield from payload["items"]
    next_page_token = payload.get("nextPageToken")

    if next_page_token is not None:
        yield from fetch_playlist_items(google_api_key,
                                        playlist_id,
                                        next_page_token)


def fetch_videos(google_api_key, playlist_id, page_token=None):
    payload = fetch_videos_pages(google_api_key, playlist_id, page_token)
    yield from payload["items"]

    next_page_token = payload.get("nextPageToken")
    if next_page_token is not None:
        yield from fetch_videos(google_api_key, playlist_id, next_page_token)


def main():
    print("Script started.")
    logging.info("START")
    google_api_key = config['google_api_key']
    playlist_id = config['playlist_key']
    for video_item in fetch_playlist_items(google_api_key, playlist_id):
        video_id = video_item["contentDetails"]["videoId"]
        for video in fetch_videos(google_api_key, video_id):
            logging.info("GOT %s", pformat(video))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
