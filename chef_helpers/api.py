from requests_oauthlib import OAuth2Session
import requests
import json
from .utils import write_response_to_file
from .utils import write_timeconf_to_file
from .utils import is_active
from .settings import secrets

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
	write_timeconf_to_file(response.json())

def refresh_oauth2_token():
	with open(secrets.LINUX_CONFIG_PATH, 'r') as infile:
		sensitive_data = json.load(infile)

	headers = {
			'content-Type': 'application/json',
	}
	data = {
			'grant_type': 'refresh_token' ,
			'refresh_token': sensitive_data['result']['data']['refresh_token'],
			'client_id': secrets.CLIENT_ID,
			'client_secret': secrets.CLIENT_SECRET,
	}
	response = requests.post(secrets.TOKEN_URL, data=json.dumps(data), headers=headers)

	write_response_to_file(response.json())
	write_timeconf_to_file(response.json())

def get_contests_list():
	with open(secrets.LINUX_CONFIG_PATH, 'r') as infile:
		sensitive_data = json.load(infile)

	headers = {
			'content-Type': 'application/json',
			'Authorization': 'Bearer ' + sensitive_data['result']['data']['access_token']
	}
	contest_list_endpoint = secrets.API_ENDPOINT + 'contests'
	response = requests.get(contest_list_endpoint, headers=headers)

	return response.json()

""" 
Returns list of active contests where each list element is a json object
"""
def get_active_contests_list():
	contests_list = get_contests_list()['result']['data']['content']['contestList']
	active_contests = []
	for contest in contests_list:
		if is_active(contest):
			active_contests.append(contest)
	return active_contests

def get_contest_rankings(contest):
	with open(secrets.LINUX_CONFIG_PATH, 'r') as infile:
		sensitive_data = json.load(infile)

	headers = {
			'content-Type': 'application/json',
			'Authorization': 'Bearer ' + sensitive_data['result']['data']['access_token']
	}
	contest_rankings_endpoint = secrets.API_ENDPOINT + 'rankings/' + contest['code']
	response = requests.get(contest_rankings_endpoint, headers=headers)
	
	return response.json()