from httpx_oauth.clients.google import GoogleOAuth2

CLIENT_ID: str = "CLIENT_ID"
CLIENT_SECRET: str = "CLIENT_SECRET"
GOOGLE_OAUTH_CLIENT = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
