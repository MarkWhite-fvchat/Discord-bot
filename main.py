import conf 
import discord
from discord.ext import commands
# intense = discord.Intents.default()
# intense.members = True
# client = discord.Client(intents=intense)


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


bot = commands.Bot(command_prefix = "!")

@bot.command(name = "hello")
async def command_hello(ctx, *args):
    if ctx.channel.id == 825339546887127081:
        msg = f'Hello, {ctx.author.name}. I am {bot.user.name} '
        await ctx.channel.send(msg)

@bot.command(name = "about_me")
async def command_about_me(ctx, *args):
    if ctx.channel.id == 825339546887127081:
        if ctx.author.nick != None:
            msg = f'Your name is {ctx.author.name}, your nick is {ctx.author.nick}'
        else:
            msg = f'Your name is {ctx.author.name}, unfortunatly, you have not a nick'
        await ctx.channel.send(msg)
    

@bot.command(name = "repeat")
async def command_repeat(ctx, *args):
    message = " ".join(args)
    if ctx.channel.id == 825339546887127081:
        msg = message
        await ctx.channel.send(msg)

@bot.command(name = "get_members")
async def command_get_members(ctx, *args):
    message = " ".join(args)
    if ctx.channel.id == 825339546887127081:
        msg = message
        await ctx.channel.send(msg)
    



bot.run(conf.bot_token)