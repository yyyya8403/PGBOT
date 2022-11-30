import discord

discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():


client.run("Tokenくれ")
