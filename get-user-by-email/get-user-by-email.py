import requests
import json
import os
from dotenv import load_dotenv

# Define the path to the root directory where .env is located
root_dir = os.path.join(os.path.dirname(__file__), '..')  # Adjust the number of '..' as needed

# Load environment variables from the .env file in the root directory
dotenv_path = os.path.join(root_dir, '.env')
load_dotenv(dotenv_path)

# Get the API key and URL from the environment variables
api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")

# Define the headers
headers = {
    'Accept': 'application/vnd.Creative Force.v2.1+json',
    'x-api-key': api_key
}

# Send the GET request
response = requests.get(api_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Define the filename for the JSON file inside the 'get-user-by-email' folder
    json_filename = os.path.join(root_dir, 'get-user-by-email', 'output.json')

    # Write the JSON data to the file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON data has been saved to {json_filename}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content if there's an error
