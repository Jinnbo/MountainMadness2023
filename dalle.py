# This example requires the 'message_content' intent.

import discord
import generateImage
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
prefix = '*'

playwords = ["draw", "start", "game"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        message.content = message.content[len(prefix):]
        prompt = message.content.split(" ")
        if prompt[0] in playwords:
            if len(prompt) == 1:
                await message.channel.send('please enter an image to be drawn')
            else:
                await message.channel.send('Drawing')
                msg = message.content[len(prompt[0]):].strip(" ")
                print(msg)
                generateImage.generateImage(msg)
                await message.channel.send(file=discord.File("1.png"))
        # print(message.content)
        # await message.channel.send('Hello!')
        
            
with open('token.txt') as f:
    lines = f.readlines()

TOKEN = lines[0]
client.run(TOKEN)

