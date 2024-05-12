import os
import discord
import asyncio
import openai

from discord import app_commands
from dotenv import load_dotenv

load_dotenv('C:\\Users\\justi\\Code\\bot\\.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# bot 
bot = discord.Client(command_prefix='/', intents=intents)
# assign a tree to bot (discord.Client)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_member_join(member):
    # do nothing when a new member joins the discord
    return

# Commands
# spray
@tree.command(name="spray", description="Spray a user being annoying",guild=discord.Object(id=639144106672652288))
async def spray_command(interaction:discord.Interaction, member:discord.Member = None):
    if member != None:
        response= f"SPRRTZ SPRRTZ SPRRTZ {member.mention}"
        await interaction.response.send_message(response)
    else:
        interaction.response.send_message("Invalid target, please enter a valid user to spray.")

# join vc
@tree.command(name="playsprtz", description="join vc and spray",guild=discord.Object(id=639144106672652288))
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
@tree.command(name="leavevc", description="force leave the vc",guild=discord.Object(id=639144106672652288))
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
    # bot tree sync
    await tree.sync(guild=discord.Object(id=639144106672652288))
    # can this be used to plant tree sync?
    guild = discord.utils.find(lambda g: g.name==GUILD, bot.guilds) 

    # track how many guilds the bot is in
    #guild_count = 0
    #for guild in bot.guilds:
    #    print(f"- {guild.name} (id: {guild.id})")
    #    guild_count = guild_count + 1

    #print(guild_count)

bot.run(TOKEN)