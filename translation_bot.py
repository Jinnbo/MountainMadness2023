# This example requires the 'message_content' intent.

import discord
import emojify
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
prefix = '$'

playwords = ["play", "start", "game"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        message.content = message.content[len(prefix):]
        arguments = message.content.split(" ")
        if arguments[0] in playwords:
            await message.channel.send('Starting game!')
            print(arguments)
        
        # print(message.content)
        # await message.channel.send('Hello!')
        
            
with open('token.txt') as f:
    lines = f.readlines()

TOKEN = lines[0]
client.run(TOKEN)


