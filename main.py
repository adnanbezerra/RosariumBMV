import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$salve maria'):
        await message.channel.send('SALVE MARIA IMACULADA!')

    if message.content.startswith('$isso'):
        await message.channel.send('Dá certo sim, chefia')

client.run('ODcwMzg1NjM4ODU4NDQ0OTAx.YQL_yw.7LOEqaW56IJB2cnI9r-NlDRdf6g')