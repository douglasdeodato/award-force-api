import os
import webbrowser
import json
from dotenv import load_dotenv

# Load environment variables from the .env file in the root project folder
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Read the account_domain from the environment variables
account_domain = os.getenv("ACCOUNT_DOMAIN")

# Read the authentication token from auth_token.json
with open("auth_token.json", "r") as json_file:
    auth_data = json.load(json_file)
    token = auth_data.get("auth_token", "")

if account_domain and token:
    # Construct the sign-in URL
    sign_in_url = f"https://{account_domain}/login?token={token}"

    # Open the sign-in URL in the default web browser
    webbrowser.open(sign_in_url)
else:
    print("ACCOUNT_DOMAIN or authentication token not found.")
