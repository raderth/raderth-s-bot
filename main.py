import discord
import os
from keep_alive import keep_alive
import random

client = discord.Client()

@client.event

async def on_ready():
  print('we have logged in as {0.user}'.format(client))

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="play.aggregate.tk"))

  

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    content = message.content
    
    if message.channel.id == 980145270882971658:
      if message.author != 979008996868517909:
        if content.startswith('!register'):
          ign_channel = client.get_channel(980159736710324315)
          other_channel = client.get_channel(980145270882971658)
          names = await ign_channel.history(limit=20).flatten()
          success = 0
          for i in names:
            if i.content == content[10:]:
              await message.channel.send('success')
              msg1 = await ign_channel.fetch_message(i.id)
              await msg1.delete()
              user = message.author
              role = discord.utils.get(user.guild.roles, name="Member")
              await user.add_roles(role)
              links = client.get_channel(980187865629720636)
              success = 1
              messages_to_delete = await other_channel.history(limit=50).flatten()
              for i2 in messages_to_delete:
                if i2.id != 982741652777099295:
                  msg = await other_channel.fetch_message(i2.id)
                  await msg.delete()
          if success == 0:
            await message.channel.send('Error: name not found, you can try again or contact support(names are caps sensitive),(ignore the console bot)')
      
    if message.channel.id == 949667606112129176:
      suggestion = client.get_channel(980825323455279114)
      embed=discord.Embed(title=content, color=discord.Color.blue())
      await suggestion.send(embed=embed)
      msg = (await suggestion.history(limit=1).flatten())[0]
      await msg.add_reaction('⬆')
      await msg.add_reaction('⬇')
      await message.delete()
      return()
      
    if not content.startswith('$'):
      return()

    if content.startswith('$'):
      await message.channel.send('That is not a valid command')
      return
    
    

keep_alive()
client.run(os.getenv("TOKEN"))