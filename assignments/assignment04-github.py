# assignment 4 - github
# author: Sylvia Chapman Kent
# reads a file from a repository, replaces all instances of the word "Andrew" with "Sylvia", then commits and pushes these changes

import requests
import json
from config import key as cfg
from git import Repo

# get key from config file and url for repository
apikey = cfg["wsaakey"]
url = "https://api.github.com/repos/rayne-fall/wsaa-private"
# get contents of repo and provide authorisation
response = requests.get(url, auth = ('token', apikey))
# read in file
with open ('text.txt', 'r') as text:
  data=text.read()
# replace Andrew with Sylvia
data=data.replace("Andrew", "Sylvia")
# write changes to file
with open ('text.txt', 'w') as text:
  text.write(data)



# 1. https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file