import discord
import os
from time import sleep
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
      ign_channel = client.get_channel(980159736710324315)
      other_channel = client.get_channel(980145270882971658)
      names = await ign_channel.history(limit=5).flatten()
      success = 0
      for i in names:
        if i.content == content:
          await message.channel.send('success')
          msg1 = await ign_channel.fetch_message(i.id)
          await msg1.delete()
          user = message.author
          role = discord.utils.get(user.guild.roles, name="Member")
          await user.add_roles(role)
          welcome = client.get_channel(978738625489563648)
          links = client.get_channel(980187865629720636)
          phrases = ["Say hello to","It's time to welcome","Give it up for","Welcome","Everyone should welcome","It's great to meet our new friend","A new member approaches"]
          USERID = message.author.id
          await links.send(f"<@{USERID}>"+ " is " +content)
          await welcome.send(random.choice(phrases)+" "+f"<@{USERID}>"+"\nWelcome to aggregate!")
          await user.edit(nick=i.content)
          success = 1
          messages_to_delete = await other_channel.history(limit=50).flatten()
          for i2 in messages_to_delete:
            if i2.id != 980152735850696794:
              msg = await other_channel.fetch_message(i2.id)
              await msg.delete()
      if success == 0:
        await message.channel.send('Error: name not found, you can try again or contact support(names are caps sensitive)')
      
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
      return
      
    user = message.author
    moderator = discord.utils.get(user.guild.roles, name="Moderator")
    
    if content.startswith('$whitelist') and moderator in user.roles: 
      action = content[11:]
      console = client.get_channel(978740611739975760)
      
      if action.startswith('add'):
        global discord_name
        welcome = client.get_channel(978738625489563648)
        name = content[15:]
        await console.send('whitelist add '+name)
        await message.channel.send('Successfully added '+name)
        link_channel = client.get_channel(980187865629720636)
        links = await link_channel.history(limit=20).flatten()
        for link in links:
          in_game_name = link.content[25:]
          if name == in_game_name:
            discord_name = link.content[0:21]
        await welcome.send("Congrats: "+discord_name+" you can now join the server on play.aggregate.tk")
        
      if action.startswith('remove'):
        name = content[18:]
        await console.send('ban '+name)
        await console.send('whitelist remove '+name)
        await message.channel.send('Successfully removed and banned '+name)
        
      if action.startswith('list'):
        await console.send('whitelist list')
        sleep(2)
        messages = await console.history(limit=5).flatten()
        for i in messages:
          if i.content.startswith('whitelist list'):
            await message.channel.send('Error: Timeout, server may be offline or lagging')
          elif i.author.id == 979008996868517909:
            await message.channel.send(i.content)
            return()
      return()

    if content.startswith('$'):
      await message.channel.send('That is not a valid command')
      return
    

    

keep_alive()
client.run(os.getenv("TOKEN"))