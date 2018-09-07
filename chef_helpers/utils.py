import os
import errno
import json
import time
from pathlib import Path
from .settings import secrets

def write_response_to_file(json_response):
	if not os.path.exists(os.path.dirname(secrets.LINUX_CONFIG_PATH)):
		try:
			os.makedirs(os.path.dirname(secrets.LINUX_CONFIG_PATH))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise

	with open(secrets.LINUX_CONFIG_PATH, "w") as outfile:
		json.dump(json_response, outfile, indent=4)

def write_timeconf_to_file(json_response):
	if not os.path.exists(os.path.dirname(secrets.TIME_CONFIG_PATH)):
		try:
			os.makedirs(os.path.dirname(secrets.TIME_CONFIG_PATH))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise

	created_time = time.time()

	time_conf = {
			'created_time': created_time,
			'expiration_time': created_time + 3600
	}

	with open(secrets.TIME_CONFIG_PATH, "w") as outfile:
		json.dump(time_conf, outfile, indent=4)

def check_if_initialized():
	if Path(secrets.LINUX_CONFIG_PATH).is_file():
		return True

	return False

def check_if_token_expired():
	with open(secrets.TIME_CONFIG_PATH, 'r') as infile:
		time_conf = json.load(infile)

	if time_conf['expiration_time'] < time.time():
		refresh_oauth2_token()