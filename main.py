import discord

key = "YOUR_API_TOKEN_HERE"

client = discord.Client()

@client.event
async def on_ready():
    print("BOT ONLINE")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("YOUR_COMMAND_HERE"):
        await message.channel.send("YOUR_RESPONSE_HERE")

client.run(key)