import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands

#-------------------DATA---------------------
bot = commands.Bot(command_prefix='!', description=None)
bot.remove_command("help")
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
permissions = discord.Permissions
underworking = ":warning: **Meh Boi, this command hasn't finished. Please wait until it's got.** :warning:"
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""
#--------------------------------------------

#-----------------SETUP----------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='🚨JailBreak🚨'))
#--------------------------------------------

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User, *, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        banneds = await bot.get_bans(ctx.message.server)
        if user not in banneds:
            bot.say("**Plz mention a banned user!**")
        else:
            room = ctx.message.channel
            await bot.unban(ctx.message.server, user)
            LogRoom = bot.get_channel(id="461623866003947520")
            await bot.say(f"**{user.mention} got unbanned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xe91e63)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, Day : int, *, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        room = ctx.message.channel
        await bot.ban(user, delete_message_days=Day)
        LogRoom = bot.get_channel(id="461623866003947520")
        await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xad1457)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User, *, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        room = ctx.message.channel
        await bot.kick(user)
        LogRoom = bot.get_channel(id="461623866003947520")
        await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓚𝓘𝓒𝓚⧸⎠╱", description=None, colour=0xe74c3c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User, duration : int, *, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        LogRoom = bot.get_channel(id="461623866003947520")
        room = ctx.message.channel
        MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.add_roles(user, MutedRole)
        await bot.say(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x11806a)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        await bot.remove_roles(user, MutedRole)
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value="Time is up...")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User, *, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        LogRoom = bot.get_channel(id="461623866003947520")
        room = ctx.message.channel
        MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.remove_roles(user, MutedRole)
        await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        
@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await bot.say(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Thats a lot!"
    elif pinges > 1000:
        mesg = "Omg, really sloooooow...."
    elif 399 > pinges > 141:
        mesg = "Ahhh, not good!"
    elif pinges < 140:
        mesg = "Its Good, Boi ;)"
    em = discord.Embed(title=None, description=f":ping_pong: Seems like `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.edit_message(msg, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, *, Reason):
    Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
    await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now locked for __{Reason}__**")
    LogRoom = bot.get_channel(id="461623866003947520")
    em = discord.Embed(title="╲⎝⧹𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x1f8b4c)
    em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
    em.add_field(name="Moderator", value=f"{ctx.message.author}")
    em.add_field(name="Reason", value=f"{Reason}")
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason):
    Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
    await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
    LogRoom = bot.get_channel(id="461623866003947520")
    em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
    em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
    em.add_field(name="Moderator", value=f"{ctx.message.author}")
    em.add_field(name="Reason", value=f"{Reason}")
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.send_message(LogRoom, embed=em)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int):
    number += 1
    deleted = await bot.purge_from(ctx.message.channel, limit=number)
    num = number - 1
    LogRoom = bot.get_channel(id="461623866003947520")
    em = discord.Embed(title=None, description=f'{ctx.message.author} deleted __{num}__ messages', colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    msg = await bot.send_message(ctx.message.channel, embed=em)
    await bot.send_message(LogRoom, embed=em)
    await asyncio.sleep(4)
    await bot.delete_message(msg)

@bot.command(pass_context=True)
async def roll(ctx, x : int, y : int):
    msg = random.randint(x, y)
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, my choose: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int, y : int):
    msg = x - y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int, y : int):
    msg = x * y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int, y : int):
    msg = x / y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int, y : int):
    msg = x ** y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int, y : int):
    msg = x + y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Oh, the result: {msg}**")
    
@bot.command()
async def game(*, play):
    await bot.change_presence(game=discord.Game(name=play))
    em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name):
    await bot.change_nickname(ctx.message.author, name)
    em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x3498db)
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def mond(ctx, *, words):
    await bot.say(f"**{words}**")

@bot.event
async def on_message(message):
    if message.content.startswith('!infó fegyók'):
        em = discord.Embed(title="INFO", description="Roblox fegyói:", colour=0x3498db)
        em.add_field(name="Pistol", value="-A kis rendőrállomáson\n-A nagy rendőrállomáson\n-A vulkán rablóbázison\n-A kis rablóállomáson", inline=False)
        em.add_field(name="Shotgun", value="-A kis rendőrállomáson\n-A nagy rendőrállomáson\n-A vulkán rablóbázison\n-A kis rablóállomáson", inline=False)
        em.add_field(name="AK-47", value="-A Kisvárosi boltban", inline=False)
        em.add_field(name="M4A1", value="-SWAT kell hozzá", inline=False)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('!infó kocsik'):
        em = discord.Embed(title="INFO", description="Roblox autói:", colour=0x3498db)
        em.add_field(name="Camaro", value="$0", inline=False)
        em.add_field(name="Helicopter", value="$0", inline=False)
        em.add_field(name="SWAT Van", value="$R", inline=False)
        em.add_field(name="PickupTruck", value="$9000", inline=False)
        em.add_field(name="Model3", value="$16000", inline=False)
        em.add_field(name="MiniCooper", value="$25000", inline=False)
        em.add_field(name="DirtBike", value="$35000", inline=False)
        em.add_field(name="SUV", value="$40000", inline=False)
        em.add_field(name="DuneBuggy", value="$45000", inline=False)
        em.add_field(name="Mustang", value="$50000", inline=False)
        em.add_field(name="Classic Car", value="$50000", inline=False)
        em.add_field(name="Quad", value="$50000", inline=False)
        em.add_field(name="Porsche", value="$70000", inline=False)
        em.add_field(name="Lamborghini", value="$100000", inline=False)
        em.add_field(name="Ferrari", value="$200000", inline=False)
        em.add_field(name="McLaren", value="$300000", inline=False)
        em.add_field(name="UFO", value="$500000", inline=False)
        em.add_field(name="Bugatti", value="$500000", inline=False)
        em.add_field(name="Monster", value="$1000000", inline=False)
        em.add_field(name="BlackHawk", value="$1000000", inline=False)
        em.add_field(name="VoltBike", value="$1000000", inline=False)
        em.set_thumbnail(url="data:image/jpeg;base64,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")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('!help'):
        emb = discord.Embed(title='MY COMMANDS:', description="Hey, check out my commands!", colour=0x3498db)
        emb.add_field(name='--------------------', value=':small_blue_diamond: r-bot\n'
                            ':white_small_square: !game {játék}\n'
                            ':small_blue_diamond: !mond {szavak}\n'
                            ':white_small_square: !ping\n'
                            ':small_blue_diamond: !sub {number1} {number2}\n'
                            ':white_small_square: !mul {number1} {number2}\n'
                            ':small_blue_diamond: !div {number1} {number2}\n'
                            ':white_small_square: !exp {number1} {number2}\n'
                            ':white_small_square: !help', inline=True)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT


token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
