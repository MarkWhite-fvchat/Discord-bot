import conf 
import discord
from discord.ext import commands
import img_handler as imhl
import os
import random
intense = discord.Intents.default()
intense.members = True
client = discord.Client(intents=intense)


# @client.event
# async def on_message(message):
    
#     #<Message 
#     # id=825338388919091200 
#     # channel=<TextChannel id=822806350886207542 
#     # name='флудильня' 
#     # position=0 
#     # nsfw=False 
#     # news=False 
#     # category_id=822806350886207539> 
#     # type=<MessageType.default: 0> 
#     # author=<Member 
#     # id=695923741732896780 
#     # name='Марк Беляков' 
#     # discriminator='8355' 
#     # bot=False nick=None 
#     # guild=<Guild 
#     # id=822806350886207538 
#     # name='Bots' 
#     # shard_id=None 
#     # chunked=False member_count=29>> flags=<MessageFlags value=0>>
#     # Защита от дурака
#     if message.author == client.user:
#         return
#     if message.author.bot:
#         return
#     if message.channel.id == 825339546887127081:
#         msg = None
#         s = message.content.split(" ", maxsplit=1)
#         # 1
#         if message.content == "/hello":
#             msg = f'Hello, {message.author.name}. I am {client.user.name} '
#         # 2
#         elif message.content == "/about_me":
#             if message.author.nick != None:
#                 msg = f'Your name is {message.author.name}, your nick is {message.author.nick}'
#             else:
#                 msg = f'Your name is {message.author.name}, unfortunatly, you have not a nick'
#         # 3
#         elif s[0] == "/repeat":
#             msg = s[1]
#         # 4
#         elif s[0] == "/get_member":
#             name = s[1]
#             if name == "":
#                 msg = f'Глупый {message.author.name}! Попробуй заново'
#             for _, member in list(enumerate(message.author.guild.members)):
#                 if name == member.name or name == member.id:
#                     msg = f'User name is {member.name} { f"And user nick is {member.nick}" if member.nick else "" } - {member.id}'
#         # 5 
#         elif message.content == "/get_members":
#             msg = ""
#             if message.author.guild.name == "Bots":
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'
#         # 6
#         elif message.content == "/get_сhannels":
#             msg = ""
#             if message.author.guild.name == "Bots":
#                 for idx, channel in list(enumerate(message.author.guild.channels)):
#                     msg += f'{idx+1}. {channel.name} - {channel.id}\n'
#         # 7
#         elif s[0] == "/goto":
#             name_channel = s[1]
#             for _, channel in list(enumerate(message.author.guild.channels)):
#                 if name_channel == channel.name or int(name_channel) == channel.id:
#                     message.channel.id = name_channel
#                     msg = f'Переход успешно завершён'
#                     break
#                 else:
#                     f'Глупый! Нет такого канала!'

#         if msg != None:
#             await message.channel.send(msg)


# client.run(conf.bot_token)
channel = 825339546887127081

bot = commands.Bot(command_prefix = "!", intents=intense)

@bot.command(name = "hello")
async def command_hello(ctx, *args):
    global channel
    if ctx.channel.id == channel:
        msg = f'Hello, {ctx.author.name}. I am {bot.user.name} '
        await ctx.channel.send(msg)

@bot.command(name = "about_me")
async def command_about_me(ctx, *args):
    global channel
    if ctx.channel.id == channel:
        if ctx.author.nick != None:
            msg = f'Your name is {ctx.author.name}, your nick is {ctx.author.nick}'
        else:
            msg = f'Your name is {ctx.author.name}, unfortunatly, you have not a nick'
        await ctx.channel.send(msg)
    

@bot.command(name = "repeat")
async def command_repeat(ctx, *args):
    global channel
    message = " ".join(args)
    if ctx.channel.id == channel:
        msg = message
        if msg=="":
            msg += "Мне нечего тебе сказать!"
        await ctx.channel.send(msg)


@bot.command(name = "get_member")
async def command_get_member(ctx, member:discord.Member=None):
    msg = ""
    global channel
    if ctx.channel.id == channel:
        if member:
            msg = f'Member {member.name} {"({member.nick})" if member.nick else ""} - {member.id}'


        if msg==None:
            msg="error"

        await ctx.channel.send(msg)



@bot.command(name = "mka")
async def command_mka(ctx, f1:discord.Member=None, f2:discord.Member=None):
    msg = ""
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            msg = f'На арене непобедимый {f1.name} против бессмертного {f2.name}!'
            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url)

            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif"))  )
        else:
            msg = "Нужно два участника!"

        if msg==None:
            msg="error"

             

@bot.command(name = "get_members")
async def command_get_members(ctx, *args):
    if ctx.channel.id == 825339546887127081:
        if ctx.author.guild.name == "Bots":
            msg = ""
            for idx, member in list(enumerate(ctx.author.guild.members)):
                msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'
        await ctx.channel.send(msg)

@bot.command(name = "get_channels")
async def command_get_сhannels(ctx, *args):
    if ctx.channel.id == 825339546887127081:
        msg = ""
        if ctx.author.guild.name == "Bots":
            for idx, channel in list(enumerate(ctx.author.guild.channels)):
                msg += f'{idx+1}. {channel.name} - {channel.id}\n'
        await ctx.channel.send(msg)


@bot.command(name = "join")
async def vc_join(ctx):
    msg = ""
    global channel
    
    if ctx.channel.id==channel:
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            msg = f'Подключаюсь к {voice_channel.name}'
            await ctx.channel.send(msg)
            await voice_channel.connect()

@bot.command(name = "leave")
async def vc_leave(ctx):
    msg = ""
    global channel
    

    if ctx.channel.id==channel:
        voice_channel = ctx.author.voice.channel
        msg = f'Отключаюсь от {voice_channel.name}'
        await ctx.channel.send(msg)
        await ctx.voice_client.disconnect()


@bot.command(name = "ost")
async def vc_ost(ctx):
    msg = ""
    global channel
    if ctx.channel.id==channel:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        msg = f'MORATL COMBAT'
        await ctx.channel.send(msg)
        await voice_client.play(discord.FFmpegPCMAudio( executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))


@bot.command(name = "fight")
async def command_fight(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel and ctx.author.voice:

        voice_channel = ctx.author.voice.channel
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if len(ctx.author.voice.channel.members) >= 2:

            mass1 = ctx.author.voice.channel.members

            a = random.randint(0, len(mass1) - 1)
            f1 = mass1.pop(a)

            b = random.randint(0, len(mass1) - 1)  
            f2 = mass1[b]

            msg = f'В бой вступают {f1.name} {f"({f1.nick})" if f1.nick else ""} и {f2.name}'

            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url, f1.name, f2.name)
            if ctx.voice_client != None:
                await ctx.voice_client.disconnect()
                await voice_channel.connect()
            else:
                await voice_channel.connect()
            await ctx.channel.send(msg)
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        else:

            f1 = ctx.author.voice.channel.members[0]
            f2 = bot.user

            msg = f'В бой вступают {f1.name} {f"({f1.nick})" if f1.nick else ""} и {f2.name}'

            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url, f1.name, f2.name)
            if ctx.voice_client != None:
                await ctx.voice_client.disconnect()
                await voice_channel.connect()
            else:
                await voice_channel.connect()
            await ctx.channel.send(msg)
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))

            
            







bot.run(conf.bot_token)