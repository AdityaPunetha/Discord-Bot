import discord

client = discord.Client()
TOKEN=ODQ1NTEyOTA1MDUwNDIzMzE3.YKiDQQ.hM6w3ih0jwSew_WhC_2vJYs0d3c

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

client.run()