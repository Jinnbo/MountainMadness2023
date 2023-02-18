# This example requires the 'message_content' intent.

import discord
import emojify
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
global right_answer


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

prefix = '$'

playwords = ["play", "start", "game"]


@client.event
async def on_message(message):
    global right_answer
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        message.content = message.content[len(prefix):]
        arguments = message.content.split(" ")
        if arguments[0] in playwords:
            await message.channel.send('Starting game!')
            print(arguments)
            right_answer = emojify.parseJSON(
                emojify.generatePhrase(), 0).lower().strip(".?,<>!@#$%^&*()")
            print(right_answer)
            emojis = emojify.parseJSON(emojify.emojiTrans(
                right_answer), 1)
            print(emojis)
            await message.channel.send(
                f"Guess the phrase from the given emojis: {emojis}")
    else:
        if right_answer is not None:
            if right_answer != "":
                if message.content.lower().strip() == right_answer.strip():
                    await message.channel.send('Correct')
                    right_answer = ""
                else:
                    await message.channel.send('Wrong')
                    # Generate a hint?
                    tmpHint = emojify.parseJSON(
                        emojify.generateHint(right_answer), 0).strip("!").strip()
                    await message.channel.send(f"Hint: {tmpHint}")


with open('token.txt') as f:
    lines = f.readlines()

TOKEN = lines[0]
client.run(TOKEN)
