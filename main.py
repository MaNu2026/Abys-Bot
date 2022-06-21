import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(mreceive):
  mreceive.content = mreceive.content.lower()
  if mreceive.author == client.user:
    return

  if mreceive.content.startswith(';hello'):
    if str(mreceive.author) == "Channie#5817":
      await mreceive.channel.send('Heyyy B! Suppp gurll?')
    else:
      await mreceive.channel.send('Hey Ola Namaste Konichiwa!')


client.run('ODU2ODc4MzA3MTMyMDQ3Mzkw.YNHcHA.taM2zH_R-DaRgp2Y7RHmBB-ALvE')
#I've changed my token number since it got compromised
