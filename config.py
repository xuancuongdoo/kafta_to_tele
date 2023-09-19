import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "google_api_key": os.environ.get("API_KEY"),
    "playlist_key": os.environ.get("PLAYLIST"),
    "kafka": {
        "bootstrap.servers": os.environ.get("BOOTSTRAP_SERVERS"),
        "security.protocol": os.environ.get("SECURITY_PROTOCOL"),
        "sasl.mechanism": os.environ.get("SASL_MECHANISM"),
        "sasl.username": os.environ.get("SASL_USERNAME"),
        "sasl.password": os.environ.get("SASL_PASSWORD")
    },
    "schema_registry": {
        "url": os.environ.get("URL"),
        "basic.auth.user.info": os.environ.get("BASIC_AUTH_USER_INFO")
    }
}
