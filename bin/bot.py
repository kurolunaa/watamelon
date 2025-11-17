import aiohttp
import os
import discord

from typing import Optional
from discord import app_commands
from dotenv import load_dotenv

# custom functions
from extra.withfwmc.withfwmc import overlayImage
from extra.date.date import convertTime
from extra.calculate_goods.calculate_goods import calculate_goods


load_dotenv()
# these need to be casted to the appropriate datatypes because os.getenv() returns a string
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER_ID = os.getenv('OWNER_ID')
BOT_ID = os.getenv('BOT_ID')
TEXTCHANNEL = int(os.getenv('TEXTCHANNEL'))
GUILD = discord.Object(id = int(os.getenv('GUILD')))

class MyClient(discord.Client):
    # Suppress error on the User attribute being None since it fills up later
    user: discord.ClientUser

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild, could be modified to fit multiple guilds via an array
        # if there are duplicate commands, uncomment the command below and run the bot, then shut the bot down and recomment it
        # self.tree.clear_commands(guild=None)
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)
        


        # this syncs to all guilds, but takes time
        # self.tree.clear_commands(guild = None) # use if there are dupes of server specific and global slash commands
        # await self.tree.sync()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

# this runs when the bot has started and has connected to discord
@client.event
async def on_ready():
    await client.change_presence(activity=discord.CustomActivity("世界で一番。強い。わためろん。", emoji = None))
    # await client.tree.sync(guild=discord.Object(id=GUILD)) # use to immediately sync commands to a server, otherwise wait ~30 minutes for it to sync to all servers
    
    # channel = client.get_channel(TEXTCHANNEL)
    # await channel.send('Successfully connected to Discord!')
    print('Successfully connected to Discord!')

    
@client.event
async def on_message(message):
    # calling things from .env need to be casted!!!!!!!
    if int(BOT_ID) == message.author.id:
        print("i just checked my own message, -1 cpu cycle gg")
        return

# CALCULATE SUBMARINE GOODS
@client.tree.command(name = "calculate_goods", description = "Calculates the amount the submarines made in gil")
@app_commands.describe(
    extravagant_salvaged_necklace = '# of Extravagant Salvaged Necklaces (34,500 gil/unit)',
    extravagant_salvaged_earring = '# of Extravagant Salvaged Earrings (30,000 gil/unit)',
    extravagant_salvaged_bracelet = '# of Extravagant Salvaged Bracelets (28,500 gil/unit)',
    extravagant_salvaged_ring = '# of Extravagant Salvaged Rings (27,000 gil/unit)',
    salvaged_necklace = '# of Salvaged Necklaces (13,000 gil/unit)',
    salvaged_earring = '# of Salvaged Earrings (10,000 gil/unit)',
    salvaged_bracelet = '# of Salvaged Bracelets (9,000 gil/unit)',
    salvaged_ring = '# of Salvaged Rings (8,000 gil/unit)'
)
async def add(interaction: discord.Interaction, extravagant_salvaged_necklace: Optional[int] = 0, extravagant_salvaged_earring: Optional[int] = 0, extravagant_salvaged_bracelet: Optional[int] = 0, extravagant_salvaged_ring: Optional[int] = 0, salvaged_necklace: Optional[int] = 0, salvaged_earring: Optional[int] = 0, salvaged_bracelet: Optional[int] = 0, salvaged_ring: Optional[int] = 0):
    """Calculates the amount of gil given the amount of extravagant and non-extravagant salvaged goods."""
    await interaction.response.send_message(calculate_goods(extravagant_salvaged_necklace, extravagant_salvaged_earring, extravagant_salvaged_bracelet, extravagant_salvaged_ring, salvaged_necklace, salvaged_earring, salvaged_bracelet, salvaged_ring))

# UNIX DATE TIME CONVERSION
@client.tree.command(name = "time", description = "Displays an offset of the current time/day given inputs")
@app_commands.describe(
    week = 'Specify how many weeks.',
    day = 'Specify how many days.',
    hour = 'Specify how many hours.',
    minute = 'Specify how many minutes.',
    second = 'Specify how many seconds.'
)
async def time(interaction: discord.Interaction, week: Optional[int], day: Optional[int], hour: Optional[int], minute: Optional[int], second: Optional[int]):
    """Displays what time/day it is with a + or - offset based on the given input."""
    await interaction.response.send_message(convertTime(week, day, hour, minute, second))

# WITH FUWAMOCO
@client.tree.context_menu(name="with FUWAMOCO-ify")
async def apply_overlay(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.defer(thinking=True)

    if not message.attachments:
        await interaction.followup.send("No image found.")
        return

    attachment = message.attachments[0]

    async with aiohttp.ClientSession() as session:
        async with session.get(attachment.url) as resp:
            img_bytes = await resp.read()

    os.makedirs("bin/extra/withfwmc/temp", exist_ok=True)
    base_path = "bin/extra/withfwmc/temp/base.png"
    overlay_path = "bin/extra/withfwmc/temp/withfwmc.png"

    with open(base_path, "wb") as f:
        f.write(img_bytes)

    result_path = overlayImage(base_path, overlay_path, scale=0.3)

    await interaction.followup.send(file=discord.File(result_path))

client.run(TOKEN)