import requests
import json
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

    # Define the folder path and filename for the JSON file
    folder_path = os.path.dirname(__file__)  # Get the path of the current script
    json_filename = os.path.join(folder_path, 'output.json')  # Adjust the filename as needed

    # Write the JSON data to the file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON data has been saved to {json_filename}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content if there's an error
