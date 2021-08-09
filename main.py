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

    # Aqui estão os comandos de orações individuais em latim
    # Eu ainda não desenvolvi o sistema para selecionar o idioma da oração.

    # Ave Maria
    if message.content.startswith('$ave-maria-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/ave.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Pater Noster
    if message.content.startswith('$pater-noster-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/pater.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Credo latim
    if message.content.startswith('$credo-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/credo.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Gloria 
    if message.content.startswith('$gloria-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/gloria.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Salve Regina
    if message.content.startswith('$salve-regina-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/salve.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Sub tuum praesidium
    if message.content.startswith('$sub-tuum-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/praesidium.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())
    
    # Oratio Fatimae
    if message.content.startswith('$oratio-la'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#latim/oratio.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Aqui estão os comandos de orações individuais em português

    # Ave Maria
    if message.content.startswith('$ave-maria-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/ave.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Pai Nosso
    if message.content.startswith('$pater-noster-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/pater.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Credo portugues
    if message.content.startswith('$credo-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/credo.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Gloria 
    if message.content.startswith('$gloria-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/gloria.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Salve Regina
    if message.content.startswith('$salve-regina-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/salve.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())

    # Sub tuum praesidium
    if message.content.startswith('$sub-tuum-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/praesidium.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())
    
    # Oratio Fatimae
    if message.content.startswith('$oratio-pt'):
        f = open('https://replit.com/@adnanmb/RosariumBMV#portugues/oratio.txt', 'r', encoding='utf8')
        await message.channel.send(f.read())
    
    # Pega citação aleatória
    if message.content.startswith('$quote'):
        await message.channel.send(getCitacao())

# Função responsável por criar as citações que serão usadas ao longo de vários momentos pelo bot
def getCitacao():
    quotes = []
    f = open('quotes/quotes.txt', 'r', encoding='utf8')
    for x in f:
        quotes.append(x)
    return (random.choice(quotes))

client.run(os.getenv('TOUKEN'))
