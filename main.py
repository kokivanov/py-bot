import json
import discord

client = discord.Client()

CONFIGS = json.load(open("settings.json"))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("Message from {0.author} at channel {0.channel} : {0.content}".format(message))

    if message.author == client.user:
        return

    if message.content.startswith(CONFIGS["PREFIX"]):
        if message.content.lower() == CONFIGS["PREFIX"]+"hi" or message.content.lower() == CONFIGS["PREFIX"]+"hello":
            await message.channel.send('Hello!')
            await message.add_reaction("<:unknown:783086103951179796>")

client.run(CONFIGS["TOKEN"])