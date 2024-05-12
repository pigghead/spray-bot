import os
import discord
import asyncio
import openai

from discord import app_commands
from dotenv import load_dotenv

load_dotenv('C:\\Users\\justi\\Code\\bot\\.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class Bot(discord.Client):
    def __init__(self, *, intents:discord.Intents):
        super().__init__(command_prefix='/', intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        print('setup_hook::syncing tree')
        res = await self.tree.sync()
        print(res)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# bot
bot = Bot(intents=intents)

# Commands

# spray
# guild=discord.Object(id=639144106672652288)
@bot.tree.command(name="spray-members", description="Spray a user being annoying",)
async def spray_command(interaction:discord.Interaction, member:discord.Member = None):
    if member != None:
        response= f"SPRRTZ SPRRTZ SPRRTZ SPRRTZ {member.mention}"
        await interaction.response.send_message(response)
    else:
        interaction.response.send_message("Invalid target, please enter a valid user to spray.")

# join vc
@bot.tree.command(name="playsprtz", description="join vc and spray",)
async def playsprtz_command(interaction:discord.Interaction):
    if(interaction.user.voice):
        channel = interaction.user.voice.channel
        vc = await channel.connect()
        await interaction.response.send_message("I am coming to spray the infidels, m'lord")
        audio_source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg.exe", source="C:\\Users\\justi\\Code\\bot\\Spray-Bottle--Short--1-www.fesliyanstudios.com.mp3"))
        audio_source.volume = 0.3
        vc.play(audio_source)
        while vc.is_playing():
            await asyncio.sleep(1)
        try:
            await interaction.followup.send("I have sprayed the nonbelievers, I am leaving now m'lord!")
            await vc.disconnect()
        except Exception as e:
            print(f"error occurred while disconnecting: {e}")
    else:
        await interaction.response.send_message("You must be in a voice channel to use this command")

# force kick bot from a vc if ever stuck
@bot.tree.command(name="leavevc", description="force leave the vc")
async def leavevc_command(interaction:discord.Interaction):
    if(interaction.guild.voice_client):
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("I am leaving the voice channel")
    else:
        await interaction.response.send_message("I am not in a voice channel")

@bot.event
async def on_message(message):
    return

# bot successfully online
@bot.event
async def on_ready():
    # sync to all command trees across multiple servers
    guild_count = 0
    for guild in bot.guilds:
        guild_count = guild_count + 1
        #await tree.sync(guild=discord.Object(guild.id))
        #await tree.sync()

    #res = await tree.sync(guild=discord.Object(id=639144106672652288))

    print(f'Spray Bot is currently in {guild_count} guilds')

    

bot.run(TOKEN)