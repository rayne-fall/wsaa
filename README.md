# Web Services and Applications

This repository contains work related to ATU Web Services and Applications Spring 2025. The code is written primarily in Python, with some HTML as well.

## Contents

[requirements.txt](requirements.txt) is a text file listing the required Python modules for the programs in this repository.

The assignments folder contains three Python programs, as well as a JSON file.

- [assignment2-carddraw.py](assignments/assignment2-carddraw.py) draws five random cards from a deck and returns the value and suit of each card.

- [assignment03-cso.py](assignments/assignment03-cso.py) retrieves the exchequer account dataset from the Central Statistics office and saves it to the [cso.json](assignments/cso.json) file.

- [assignment04-github.py](assignments/assignment04-github.py) retrieves a text file from a private repository, replaces all instances of the word "Andrew" with the word "Sylvia", then commits and pushes these changes to the repository.

The project folder currently contains a Flask server.

## Running the programs

Most of the programs can be run either locally using [Anaconda](https://www.anaconda.com/download) and [Visual Studio Code](https://code.visualstudio.com/), or online using [Github Codespaces](https://github.com/features/codespaces). 

[assignment04-github.py](assignments/assignment04-github.py) is the exception. Attempting to run this program in Codespaces will cause issues as the required keys should be stored only on the user's local machine for security and will not be accessible in Codespaces.

### Running locally

1. Clone the repository.
1. Use Anaconda to set up the environment.
1. Launch Visual Studio Code.
1. Install the modules listed in the [requirements.txt](requirements.txt) file.
1. Run the script.

### Running in Codespaces

1. Click the green "Code" button at the top of the main repository page.
1. Click "Open with Codespaces".
1. Once the codespace has loaded, run the script in the browser.