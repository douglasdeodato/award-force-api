import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key and URL from the environment variables
api_key_external = os.getenv("API_KEY_EXTERNAL")
api_url_external = os.getenv("API_URL_EXTERNAL")

# Define the headers
headers = {
    'Accept': 'application/vnd.Creative Force.v2.1+json',
    'x-api-key': api_key_external
}

# Send the GET request
response = requests.get(api_url_external, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Print the JSON response
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content if there's an error
