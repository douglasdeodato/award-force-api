# get-user-by-email

API_KEY=api_here

API_URL=https://api.cr4ce.com/user/email@gmail.com


I provide the email to get the slug.


# get-slug-token

# run1-get-user-by-email.py
I am Provinding the email.
this will generate the slug

# run2-get-auth-token.py
with the slug I will get auth token.

Constructed URL: https://api.cr4ce.com/user/SLUG/auth-token
Authentication Token: auth-token-generated

# run3-auto_sign_in.py

with the token I will redirect to the login page 
sign_in_url = f"https://{account_domain}/login?token={token}"



# sample .env file


API_KEY= 
API_URL=https://api.cr4ce.com/user/email@gmail.com

API_KEY_EXTERNAL= 
API_URL_EXTERNAL=https://api.cr4ce.com/user/slughere/auth-token


ACCOUNT_DOMAIN=domain-name-here


# SSO sample .env file

API_KEY= 
API_KEY_EXTERNAL= 
ACCOUNT_DOMAIN=site-name-here
