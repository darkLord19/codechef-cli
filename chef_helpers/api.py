from requests_oauthlib import OAuth2Session
import requests
import json
from .settings import secrets

def new_oauth2_token():
        
	chef = OAuth2Session(secrets.client_id)
	access_url, state = chef.authorization_url(secrets.authorization_url)
	print('Please go here and authorize,', access_url)
	redirect_response = input('Paste the output shown on redirected URL here:')
	headers = {
			'content-Type': 'application/json',
	}
	data = {
			'grant_type': 'authorization_code',
			'code': redirect_response,
			'client_id': secrets.client_id,
			'client_secret': secrets.client_secret,
	}
	response = requests.post(secrets.token_url, data=json.dumps(data), headers=headers)
	
	write_response_to_file(response)