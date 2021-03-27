import conf 
import discord
client = discord.Client()


@client.event
async def on_message(message):
    #<Message 
    # id=825338388919091200 
    # channel=<TextChannel id=822806350886207542 
    # name='флудильня' 
    # position=0 
    # nsfw=False 
    # news=False 
    # category_id=822806350886207539> 
    # type=<MessageType.default: 0> 
    # author=<Member 
    # id=695923741732896780 
    # name='Марк Беляков' 
    # discriminator='8355' 
    # bot=False nick=None 
    # guild=<Guild 
    # id=822806350886207538 
    # name='Bots' 
    # shard_id=None 
    # chunked=False member_count=29>> flags=<MessageFlags value=0>>
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if message.channel.id == 825339546887127081:
        msg = None
        if message.content == "/hello":
            msg = f'Hello, {message.author.name}. I am {client.user.name} '
        elif message.content == "/about_me":
            if message.author.nick != None:
                msg = f'Your name is {message.author.name}, your nick is {message.author.nick}'
            else:
                msg = f'Your name is {message.author.name}, unfortunatly, you have not a nick'
        if msg != None:
            await message.channel .send(msg)


client.run(conf.bot_token)