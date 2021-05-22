import discord
import os
import requests
import json
import random

client = discord.Client()

'''REPLACE TOKEN WITH os.environ['TK'] REPLACE TOKEN WITH os.environ['TK'] REPLACE TOKEN WITH os.environ['TK'] '''

TOKEN = 'ODQ1NTEyOTA1MDUwNDIzMzE3.YKiDQQ.hM6w3ih0jwSew_WhC_2vJYs0d3c'

'''REPLACE TOKEN WITH os.environ['TK'] REPLACE TOKEN WITH os.environ['TK'] REPLACE TOKEN WITH os.environ['TK'] '''

sad_words = ["sad", "depressed", "unhappy", 'angry', 'miserable', 'depressing']
starter_encouragements = ['Cheer up!', 'Hang in there']


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    if message.content.startswith('$inspire'):
        await message.channel.send(get_quote())
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


client.run(TOKEN)
