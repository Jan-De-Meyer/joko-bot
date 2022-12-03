import discord
import os
import random
from discord.utils import get
from discord.ext import commands
import time
import json
import os
import re

client = discord.Client()
bot = commands.Bot(command_prefix = '.')
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

level_dict = {
    "lvl1" : 100,
    "lvl2": 200,
    "lvl3": 300,
    "lvl4": 500,
    "lvl5": 800,
    "lvl6": 1300,
    "lvl7": 2800,
    "lvl8": 4100,
    "lvl9": 6900,
    "lvl10": 11000,
    "lvl11": 17900,
    "lvl12": 28900,
    "lvl13": 37800,
    "lvl14": 66700,
    "lvl15": 104500,
    "lvl16": 171200
  }

async def purge_channel():
    channel = client.get_channel(998288326983430194)
    messages = []
    await channel.send("sweepity swoopity")
    async for message in channel.history(limit=100000):
        time.sleep(2)
        await message.delete()






def checking_xp_db():
#checks if json list with xp exists if not make it and fill it up
    if os.path.exists('xp.json'):
        if os.stat('xp.json').st_size == 0:
            guild = client.get_guild(997993719879979028)
            members_list = guild.members
            y ={}
            for x in members_list:
                y[x.name] = 0 
            y = json.dumps(y, indent=2, sort_keys=True)
            with open('xp.json', 'w') as outfile:
                outfile.write(y)
    else:
        with open('xp.json', 'w') as file:
            pass
        checking_xp_db()

def checking_lvl_db():
    if os.path.exists('lvl.json'):
        if os.stat('lvl.json').st_size == 0:
            guild = client.get_guild(997993719879979028)
            members_list = guild.members
            y ={}
            for x in members_list:
                y[x.name] = 0 
            y = json.dumps(y, indent=2, sort_keys=True)
            with open('lvl.json', 'w') as outfile:
                outfile.write(y)
    else:
        with open('lvl.json', 'w') as file:
            pass
        checking_lvl_db()

def checking_members():
    #checks members list and adds new people every new message
    guild = client.get_guild(997993719879979028)
    members_list = guild.members #kinda useless imo
    x =[]
    with open('xp.json', 'r') as openfile:
        y = json.load(openfile)
    z = list(y.keys())
    for _ in members_list:
        x.append(_.name)
    x.sort()
    if x != z:
        for item in x:
            if item not in z :
                y[item] = 0
    y = json.dumps(y, indent=2, sort_keys=True)
    with open('xp.json', 'w') as outfile:
                outfile.write(y)

async def increase_xp(message):
    xp = random.choice([1,2,3,4,5,6,7,8,9,10])
    with open('xp.json', 'r') as openfile:
        y = json.load(openfile)
    current_xp = y[message.author.name]
    y[message.author.name] = current_xp + xp
    if current_xp + xp > 100:
        with open('lvl.json', 'r') as openfile:
            y = json.load(openfile)
            current_lvl = y[message.author.name]
            new_lvl = current_lvl + 1
            y[message.author.name] = current_lvl + 1
            y = json.dumps(y, indent=2, sort_keys=True)
            #with open('lvl.json', 'w') as outfile:
            #    outfile.write(y)
            #if new_lvl <= 3:        
            #    await message.channel.send(f'oh you did it {message.author.name}? finally {new_lvl}, GET BACK TO WORK!')
            #elif new_lvl <= 6:
            #    await message.channel.send(f'impressive {message.author.name}, level{new_lvl} but how much higher can you go ?')
            #elif new_lvl <= 10:
            #    await message.channel.send(f'finally an ascension worth my attention {message.author.name}, level{new_lvl} is no small feat.')
            #else:
            #    await message.channel.send(f'its palawa for you {message.author.name},level {new_lvl} keep going.')
        with open('xp.json', 'r') as openfile:
            y = json.load(openfile)
            y[message.author.name] = 0
            y = json.dumps(y, indent=2, sort_keys=True)
        with open('xp.json', 'w') as outfile:
            outfile.write(y)
    else:
        y[message.author.name] = current_xp + xp
        y = json.dumps(y, indent=2, sort_keys=True)
        with open('xp.json', 'w') as outfile:
            outfile.write(y)
    

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    ##checking_xp_db()
    ##checking_lvl_db()
    ##checking_members()
    #purge_channel()

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord server!')
    ##checking_xp_db()
    ##checking_lvl_db()
    ##checking_members()


#the funny haha joko responded function
@client.event
async def on_message(message):
    await increase_xp(message)
    if message.author.id != "998287158550990968":
        print('inside if statement')
        pattern = re.compile(r"^praise joko!?$", re.IGNORECASE)
        print(pattern)
        result = pattern.match(message.content)
        print('content checked')
        print(result)
        if result:
            x=('please, call me palawa OwO','you better.', 'my loyal subjects...', 'your king loves you.','Oh-ho, Commander. You DO know how to flatter a lich.', "It's funny, I remember you being taller. And better looking."," It's an honor to die by Joko's hand. Usually I delegate." )
            await message.add_reaction('❤️‍🔥')
            async with message.channel.typing():
                time.sleep(2)
            await message.channel.send(random.choice(x))
    
    
    if message.content.startswith('.clean'):
       await purge_channel()
    
    
    if message.content.startswith('.spam'):
        for _ in message.author.roles:
            for x in range(0,1000):
                await message.channel.send("<@178588642661367810>")



    #if message.contente:
    #    print('inside if statement')
     #   pattern = "/praise joko/gi"
    #    result = re.match(pattern, message.content)
    #    if result:
    #        x=('please, call me palawa OwO','you better.', 'my loyal subjects...', 'your king loves you.','Oh-ho, Commander. You DO know how to flatter a lich.', "It's funny, I remember you being taller. And better looking."," It's an honor to die by Joko's hand. Usually I delegate." )
    #        await message.add_reaction('❤️‍🔥')
    #        async with message.channel.typing():
    #            time.sleep(2)
    #        await message.channel.send(random.choice(x))
    
    if message.content.startswith('.roles'):
        #part of the roles function pretty much finished
        await message.author.send('click the hearts and get roles!')
        dm = await message.author.send('💚 = Fractals, 🧡 = raids, ❤️ = PvP, 🖤 = WvW')
        await dm.add_reaction('💚')
        await dm.add_reaction('🧡')
        await dm.add_reaction('❤️')
        await dm.add_reaction('🖤')
    
    
    if message.content.startswith('the turkies must rise up!'):
        await message.channel.send('https://cdn.discordapp.com/attachments/268400938799071232/998551649666748466/v12044gd0000cau7c53c77u2cof7k460.mp4')
    
    if message.content.startswith('spawn leduude'):
        await message.channel.send('https://cdn.discordapp.com/attachments/439519668819066880/1043121778169491546/meintochat.mp4')
    
    if message.content.startswith('blacks'):
        await message.channel.send('1045487523041918976')


@client.event
async def on_raw_reaction_add(payload):
    #roles function within bot wip
    emoji_dict={
        '💚' : 'Fractals',
        '🧡' : 'Raids',
        '❤️' : 'PvP',
        '🖤' : 'WvW'
    }

    if payload.user_id != 998287158550990968:
        print(emoji_dict[payload.emoji.name])
        requested_role = emoji_dict[payload.emoji.name]
        server = client.get_guild(997993719879979028)
        user = await server.fetch_member(payload.user_id)
        role = discord.utils.find(lambda x: x.name == requested_role, server.roles)
        await user.add_roles(role)





        
client.run("YOUR KEY HERE")
