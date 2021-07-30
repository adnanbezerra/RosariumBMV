import discord
import os
import random

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

    if message.content.startswith('$salve'):
        await message.channel.send('Salve Regina, Mater Misericordiae!')

    if message.content.startswith('$isso'):
        await message.channel.send('Dá certo sim, chefia')

    # Aqui estão os comandos de orações individuais em latim
    # Eu ainda não desenvolvi o sistema para selecionar o idioma da oração.

    # Ave Maria
    if message.content.startswith('$ave-maria-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/ave.txt', 'r')
        await message.channel.send(f.read())

    # Pater Noster
    if message.content.startswith('$pater-noster-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/pater.txt', 'r')
        await message.channel.send(f.read())

    # Credo latim
    if message.content.startswith('$credo-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/credo.txt', 'r')
        await message.channel.send(f.read())

    # Gloria 
    if message.content.startswith('$gloria-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/gloria.txt', 'r')
        await message.channel.send(f.read())

    # Salve Regina
    if message.content.startswith('$salve-regina-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/salve.txt', 'r')
        await message.channel.send(f.read())

    # Sub tuum praesidium
    if message.content.startswith('$sub-tuum-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/praesidium.txt', 'r')
        await message.channel.send(f.read())
    
    # Oratio Fatimae
    if message.content.startswith('$oratio-la'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/latim/oratio.txt', 'r')
        await message.channel.send(f.read())

    # Aqui estão os comandos de orações individuais em português

    # Ave Maria
    if message.content.startswith('$ave-maria-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/ave.txt', 'r')
        await message.channel.send(f.read())

    # Pater Noster
    if message.content.startswith('$pater-noster-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/pater.txt', 'r')
        await message.channel.send(f.read())

    # Credo latim
    if message.content.startswith('$credo-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/credo.txt', 'r')
        await message.channel.send(f.read())

    # Gloria 
    if message.content.startswith('$gloria-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/gloria.txt', 'r')
        await message.channel.send(f.read())

    # Salve Regina
    if message.content.startswith('$salve-regina-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/salve.txt', 'r')
        await message.channel.send(f.read())

    # Sub tuum praesidium
    if message.content.startswith('$sub-tuum-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/praesidium.txt', 'r')
        await message.channel.send(f.read())
    
    # Oratio Fatimae
    if message.content.startswith('$oratio-pt'):
        f = open('C:/Users/adnan/Documents/RosariumBMV/portugues/oratio.txt', 'r')
        await message.channel.send(f.read())
    
    # Pega citação aleatória
    if message.content.startswith('$quote'):
        quotes = []
        f = open('C:/Users/adnan/Documents/RosariumBMV/quotes/quotes.txt', 'r', encoding='utf8')
        for x in f:
            quotes.append(x)
        await message.channel.send(random.choice(quotes))
        f.close()

client.run('o token nem tá aqui, coleguinha :/')
