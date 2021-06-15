# Clinical 
### An automation tool for the [SoccerGuru discord bot](https://top.gg/bot/668075833780469772).

## Features
- Automates hourly claiming of players, arena matches
- User Configurability
- Runs in the background, even when Discord is closed
- More features coming soon


## Setup

### Installations
1. Run ``pip3 install requests`` 
2. Run ``pip3 install pyyaml``

### Configuration
Open ``config.yml`` and update it with the correct information.

- Empty fields need to be filled in. 
- **DO NOT** remove quotation marks.
- Update ``prefix`` with the correct bot prefix in the server of your choice. 
- Update ``arena`` with either 'y' or 'n' (yes or no). This decides whether arena matches are automated.

### Retrieving Authorisation Token (field: ``authorization``)
1. Open Discord on your browser, logged into the account you intend to use, and go to the channel you intend to enter commands (preferably a private server)
2. Open the inspector by pressing F12 or ctrl + shift + i
3. Click the “Network” tab
4. Locate an entry called “science” and click on it
5. Locate “Response Headers” and copy the value found at “authorization”. That is your token.

### Retrieving Channel ID (field: ``channel``)
1. Open Discord user settings > Advanced > Turn on Developer Mode
2. Right click on the correct channel and copy its channel ID

## Usage
1. Open the terminal of your choice in the correct directory and enter ``python3 main.py``
2. To stop the tool, press ctrl + c in the terminal.

- Discord need not be open for the tool to run.
- Leave the terminal open.



