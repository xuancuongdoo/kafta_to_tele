#!/usr/bin/env python

import logging
import sys
import requests
from config import config


def main():
    print("Script started.")
    logging.info("START")
    google_api_key = config["google_api_key"]
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": google_api_key
        })

    logging.debug("GOT %s", response.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
