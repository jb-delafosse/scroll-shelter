from app.config import get_config
from httpx_oauth.clients.google import GoogleOAuth2

config = get_config()


CLIENT_ID: str = config.client_id
CLIENT_SECRET: str = config.client_secret
GOOGLE_OAUTH_CLIENT = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
