import os
import requests
import json
from dotenv import load_dotenv
from flask import Flask, request, render_template_string, send_from_directory

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Define the API key from the .env file
api_key = os.getenv("API_KEY")

# Define the headers
headers = {
    'Accept': 'application/vnd.Creative Force.v2.1+json',
    'x-api-key': api_key
}

# Define a debugging mode flag
debug_mode = False

# Define a template for the web form
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>API Request</title>
</head>
<body>
    <h1>API Request</h1>
    <form method="post">
        <label for="email">Enter your email address:</label>
        <input type="text" id="email" name="email" required><br><br>
        <input type="submit" value="Submit">
    </form>
    <br>
    {% if response_data %}
    <h2>Response Data:</h2>
    <pre>{{ response_data }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def api_request():
    global debug_mode

    if request.method == 'POST':
        user_email = request.form['email']
        api_url = f"https://api.cr4ce.com/user/{user_email}"

        response = requests.get(api_url, headers=headers)

        if debug_mode:
            print(f"API URL: {api_url}")
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            response_data = json.dumps(data, indent=4)
            # Save the JSON data to slug.json
            with open('slug.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
        else:
            response_data = f"Request failed with status code: {response.status_code}\n{response.text}"
    else:
        response_data = None

    return render_template_string(form_template, response_data=response_data)

@app.route('/slug.json')
def download_json():
    # Serve the saved slug.json file
    return send_from_directory('.', 'slug.json')

if __name__ == '__main__':
    debug_mode = True  # Set debug_mode to True when running locally for debugging
    app.run(debug=True)
