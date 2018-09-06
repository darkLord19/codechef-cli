import os
import errno
import json
from settings import secrets

def write_response_to_file(json_response):
    if not os.path.exists(os.path.dirname(secrets.LINUX_CONFIG_PATH)):
        try:
            os.makedirs(os.path.dirname(secrets.LINUX_CONFIG_PATH))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(secrets.LINUX_CONFIG_PATH, "w") as outfile:
        json.dump(json_response, outfile, indent=4)