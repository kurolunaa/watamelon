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
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER_ID = os.getenv('OWNER_ID')
BOT_ID = os.getenv('BOT_ID')
TEXTCHANNEL = int(os.getenv('TEXTCHANNEL')) # Cast to an int because os.getenv returns a string
GUILD = discord.Object(id = int(os.getenv('GUILD')))

# this makes it so i don't have to manually specify a guild for every tree command
# copied from discord.py repo
class MyClient(discord.Client):
    # Suppress error on the User attribute being None since it fills up later
    user: discord.ClientUser

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

# this runs when the bot has started and has connected to discord
@client.event
async def on_ready():
    await client.change_presence(activity=discord.CustomActivity("世界で一番。強い。わためろん。", emoji = None))
    # await client.tree.sync(guild=discord.Object(id=GUILD)) # use to immediately sync commands to a server, otherwise wait ~30 minutes for it to sync to all servers
    # tree.clear_commands(guild = GUILD) # use if there are dupes of server specific and global slash commands
    print('Successfully connected to Discord!')
    
    # channel = client.get_channel(TEXTCHANNEL)
    # await channel.send('Successfully connected to Discord!')

    
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
@client.tree.command(name = "convert_time", description = "Converts specified time to a Unix timestamp")
@app_commands.describe(
    year = 'Specify the year (1 - 9999), leave blank for current year.', 
    month = 'Specify the month (1 - 12), leave blank for current month.',
    day = 'Specify the day (1 - 31), leave blank for current day.',
    hour = 'Specify hour (0 - 23), leave blank for current hour.',
    minute = 'Specify minutes (0 - 59), leave blank for current minutes.',
    second = 'Specify seconds (0 - 59), leave blank for current seconds.'
)
async def convert_time(interaction: discord.Interaction, year: Optional[int], month: Optional[int], day: Optional[int], hour: Optional[int], minute: Optional[int], second: Optional[int]):
    """Converts a specified time to Unix timestamp, leave blank for current time."""
    await interaction.response.send_message(convertTime(year, month, day, hour, minute, second))

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