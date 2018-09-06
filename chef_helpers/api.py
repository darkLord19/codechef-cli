from requests_oauthlib import OAuth2Session
import requests
import json
from settings import secrets
from utils import write_response_to_file

def new_oauth2_token():
        
	chef = OAuth2Session(secrets.CLIENT_ID)
	access_url, state = chef.authorization_url(secrets.AUTHORIZATION_URL)
	print('Please go here and authorize,', access_url)
	redirect_response = input('Paste the output shown on redirected URL here:')
	
	headers = {
			'content-Type': 'application/json',
	}
	data = {
			'grant_type': 'authorization_code',
			'code': redirect_response,
			'client_id': secrets.CLIENT_ID,
			'client_secret': secrets.CLIENT_SECRET,
	}
	response = requests.post(secrets.TOKEN_URL, data=json.dumps(data), headers=headers)
	
	write_response_to_file(response.json())