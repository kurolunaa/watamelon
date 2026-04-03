# watamelon Discord Bot

A Discord bot (primarily) designed to calculate and (soon) visualize submarine goods in the popular MMORPG Final Fantasy XIV. 

## Usage
LINUX:<br>
```
chmod +x start_server.sh
./start_server.sh
```

## Installation <hr>
Create a python virtual environment (venv):<br>
```
python3 -m venv .venv
```

Then, in a terminal of your choice, enter your venv environment then pip install the requirements.txt:<br>
``` 
source .venv/bin/activate
pip install -r requirements.txt 
```

### .env <hr>
Be sure to include a `.env` file in the root of your folder.<br>

Example contents of `.env` file:
```
DISCORD_TOKEN=
OWNER_ID=
BOT_ID=
TEXTCHANNEL=
GUILD=
```