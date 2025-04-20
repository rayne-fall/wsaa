# assignment 4 - github
# author: Sylvia Chapman Kent
# reads a file from a repository, replaces all instances of the word "Andrew" with "Sylvia", then commits and pushes these changes

import requests
import json
from config import key as cfg

# get key from config file and url for repository
apikey = cfg["wsaakey"]
url = "https://api.github.com/repos/rayne-fall/wsaa-private"
# get contents of repo and provide authorisation
response = requests.get(url, auth = ('token', apikey))
