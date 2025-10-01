import os
import discord
from discord import app_commands

from dotenv import load_dotenv

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
async def add(interaction: discord.Interaction, extravagant_salvaged_necklace: int, extravagant_salvaged_earring: int, extravagant_salvaged_bracelet: int, extravagant_salvaged_ring: int, salvaged_necklace: int, salvaged_earring: int, salvaged_bracelet: int, salvaged_ring: int):
    """Calculates the amount of gil given the amount of extravagant and non-extravagant salvaged goods."""

    output = ""

    if extravagant_salvaged_necklace > 0:
        output += f"{extravagant_salvaged_necklace}x Extravagant Salvaged Necklaces = {extravagant_salvaged_necklace * 34500:,d} gil\n"
    if extravagant_salvaged_earring > 0:
        output += f"{extravagant_salvaged_earring}x Extravagant Salvaged Earrings = {extravagant_salvaged_earring * 30000:,d} gil\n"
    if extravagant_salvaged_bracelet > 0:
        output += f"{extravagant_salvaged_bracelet}x Extravagant Salvaged Bracelets = {extravagant_salvaged_bracelet * 28500:,d} gil\n"
    if extravagant_salvaged_ring > 0:
        output += f"{extravagant_salvaged_ring}x Extravagant Salvaged Rings = {extravagant_salvaged_ring * 27000:,d} gil\n"
    if salvaged_necklace > 0:
        output += f"{salvaged_necklace}x Salvaged Necklaces = {salvaged_necklace * 13000:,d} gil\n"
    if salvaged_earring > 0:
        output += f"{salvaged_earring}x Salvaged Earrings = {salvaged_earring * 10000:,d} gil\n"
    if salvaged_bracelet > 0:
        output += f"{salvaged_bracelet}x Salvaged Bracelets = {salvaged_bracelet * 9000:,d} gil\n"
    if salvaged_ring > 0:
        output += f"{salvaged_ring}x Salvaged Rings = {salvaged_ring * 8000:,d} gil\n"

    if output == "":
        output = "subs made no money :("
        await interaction.response.send_message(output)
        return

    output += f"Total amount obtained on this trip: **{((extravagant_salvaged_necklace * 34500) + (extravagant_salvaged_earring * 30000) + (extravagant_salvaged_bracelet * 28500) + (extravagant_salvaged_ring * 27000) + (salvaged_necklace * 13000) + (salvaged_earring * 10000 ) + (salvaged_bracelet * 9000) + (salvaged_ring * 8000)):,d} gil**"
    await interaction.response.send_message(output)

client.run(TOKEN)