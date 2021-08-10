import discord
from os import getenv
from random import choice

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for $rezar'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Aqui estão os comandos de orações individuais em latim
    # Eu ainda não desenvolvi o sistema para selecionar o idioma da oração.

    # Ave Maria
    if message.content.startswith('$'):
      if message.content == '$salve':
        await message.channel.send('Salve Regina, Mater Misericordiae!')
        return
      if message.content == '$pray':
        return
      if message.content == '$quote':
        await message.channel.send(getCitacao())
      else:
        mensagem = message.content
        with open(retornaOracao(mensagem), 'r', encoding='utf8') as f:
            await message.channel.send(f.read())


# Função responsável por criar as citações que serão usadas ao longo de vários momentos pelo bot
def getCitacao():
    quotes = []
    with open('quotes/quotes.txt', 'r', encoding='utf8') as f:
        for x in f:
            quotes.append(x)

    return (choice(quotes))

entradas = {
  '$ave-maria-la': 'latim/ave.txt',
  '$pater-noster-la': 'latim/pater.txt',
  '$credo-la': 'latim/credo.txt',
  '$gloria-la': 'latim/gloria.txt',
  '$salve-regina-la': 'latim/salve.txt',
  '$sub-tuum-la': 'latim/praesidium.txt',
  '$oratio-la': 'latim/oratio.txt',
  '$ave-maria-pt': 'portugues/ave.txt',
  '$pater-noster-pt': 'portugues/pater.txt',
  '$credo-pt': 'portugues/credo.txt',
  '$gloria-pt': 'portugues/gloria.txt',
  '$salve-regina-pt': 'portugues/salve.txt',
  '$sub-tuum-pt': 'portugues/praesidium.txt',
  '$oratio-pt': 'portugues/oratio.txt',
}

def retornaOracao(entrada):
  return entradas[entrada]

client.run(getenv('TOUKEN'))
