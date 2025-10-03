# Spray Bot

Playful **Discord Bot** built with [discord.py](https://discordpy.readthedocs.io/en/stable/) that lets you "spray" annoying members in chat or voice channels

Supports several **slash commands (/)**, and can even join a voice channel to play audio.

## Features
- `/spray-members @user`: spray a targeted member in chat with a 'SPRTZ' message
- `/playsprtz`: bot joins your voice channel and plays a water bottle spray sound effect
- `/leavevc`: force bot to leave the vc in case it hangs

## Tech Stack
- **Python 3.9**
- [discord.py 2.x (with app_commands)](https://discordpy.readthedocs.io/en/stable/interactions/api.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [FFmpeg](https://ffmpeg.org/)

## Setup & Installation
### 1. Clone repo
```bash
git clone https://github.com/pigghead/spray-bot.git
cd spray-bot
```

### 2. (Optional) Create & activate a virtual environment
```
python -m venv venv

# windows
venv\Script\activate

# mac/ linux
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Install FFmpeg
- Download and install [FFmpeg](https://ffmpeg.org/)
- Ensure executable path matches whats in the code (i.e. Windows: C:/ffmpeg/ffmpeg.exe)

### 5. Configure environment variables
Creat a .env file in the root of the project with the following variables
```env
DISCORD_TOKEN=[you-discord-bot-token]
DISCORD_GUILD=[your-discord-guild-id]  # optional; this is just the server id
```

### 6. Run the bot
```bash
python main.py
```

## Notes
- Requires Discord Intents: `members`, `message_content`
- Ensure bot has permission to connect and speak in voice channels
- Sound effect path is hard coded:
```
C:\Users\justi\Code\bot\Spray-Bottle--Short--1-www.fesliyanstudios.com.mp3
```
Change this to your desired sound effect

## Next Steps/ Ideas
- Docker container for easier deployment
- Externalize audio file into config
- Error handling for permission issues
