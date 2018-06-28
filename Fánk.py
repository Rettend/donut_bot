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
    if message.content.upper().startswith('!INFÓ PISTOL'):
        em = discord.Embed(title="INFO", description="Pistol:", colour=0x3498db)
        em.add_field(name="Előfordulás:", value="-A kis rendőrállomáson\n-A nagy rendőrállomáson\n-A vulkán rablóbázison\n-A kis rablóállomáson", inline=False)
        em.add_field(name="Ismertető:", value="Nagy sebzésű fegyver, egy játékos életének 16%-át veszi le egy lövéssel, 8 lövedék van egy tárban és a tárat max. 4 másodperc alatt üríti ki. Nagy látótávolsága miatt gyakran használják járművek megállítására", inline=False)
        em.set_image(url="https://vignette.wikia.nocookie.net/rblx-jailbreak/images/a/a1/Pistol_template.png/revision/latest?cb=20170712041824")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(message.channel, embed=em)
    if message.content.upper().startswith('!INFÓ SHOTGUN'):
        em = discord.Embed(title="INFO", description="Shotgun:", colour=0x3498db)
        em.add_field(name="Előfordulás:", value="-A kis rendőrállomáson\n-A nagy rendőrállomáson\n-A vulkán rablóbázison\n-A kis rablóállomáson", inline=False)
        em.add_field(name="Ismertető:", value="Kis látótávolságával a közeli csatákhoz a legjobb fegyver, sebzése nem kiszámítható de akár 3 lövéssel is megölhet egy játékost. 4 lövedék van egy tárban.", inline=False)
        em.set_image(url="https://vignette.wikia.nocookie.net/rblx-jailbreak/images/3/31/Shotgun_template.png/revision/latest?cb=20170712043016")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(message.channel, embed=em)
    if message.content.upper().startswith('!INFÓ AK-47'):
        em = discord.Embed(title="INFO", description="Shotgun:", colour=0x3498db)
        em.add_field(name="Előfordulás:", value="-A Kisvárosi boltban", inline=False)
        em.add_field(name="Ismertető:", value="A pisztolynál kisebb látótávval rendelkező fegyver, nagyon kicsi a sebzése, egy lövés a játékos életének 2%-át veszi le. Főleg járművek gyors megállítására használják", inline=False)
        em.set_image(url="https://vignette.wikia.nocookie.net/rblx-jailbreak/images/e/e8/Ak47_template.png/revision/latest?cb=20170712043521")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(message.channel, embed=em)
    if message.content.upper().startswith('!INFÓ M4A1'):
        em = discord.Embed(title="INFO", description="M4A1:", colour=0x3498db)
        em.add_field(name="Előfordulás:", value="-SWAT-osok számára elérhető a kis- és nagyrendőrállomáson", inline=False)
        em.add_field(name="Ismertető:", value="A legjobb fegyver, nagy látótávolsága van. 20 lövedék van egy tárban és 1 tárral képes megolni egy játékost. Teljesen automata fegyver.", inline=False)
        em.set_image(url="https://vignette.wikia.nocookie.net/rblx-jailbreak/images/9/94/M4A1_template.png/revision/latest?cb=20170712042300")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(message.channel, embed=em)
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
