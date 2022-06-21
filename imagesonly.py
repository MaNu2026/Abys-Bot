import discord

client = discord.Client()

@client.event
async def on_message(message):
  if str(message.channel) == "imagesonly" and message.content != "":
    await message.channel.purge(limit=1)

client.run('ODU2ODc4MzA3MTMyMDQ3Mzkw.YNHcHA.taM2zH_R-DaRgp2Y7RHmBB-ALvE')
