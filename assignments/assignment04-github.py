# assignment 4 - github
# author: Sylvia Chapman Kent
# reads a file from a repository, replaces all instances of the word "Andrew" with "Sylvia", then commits and pushes these changes

import requests
from config import key as cfg
from github import Github

# get key from config file
apikey = cfg["wsaakey"]
# get contents of repo and provide authorisation
g=Github(apikey)
repo=g.get_repo('rayne-fall/wsaa-private')
file=repo.get_contents('text.txt')
url=file.download_url
response = requests.get(url)
file_contents=response.text
# read in file
with open (file_contents, 'r') as text:
  data=text.read()
# replace Andrew with Sylvia
data=data.replace("Andrew", "Sylvia")
# write changes to file
with open (file_contents, 'w') as text:
  text.write(data)
# commit and push changes  
github_response=repo.update_file(file.path,'replaced Andrew with Sylvia',response,file.sha)
print(github_response)


# 1. https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file