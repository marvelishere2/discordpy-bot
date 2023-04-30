# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
from discord import app_commands
import discord.utils


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(client)
bot.remove_command('help')



@bot.event
async def on_ready():
    print('{0.user} is ready'.format(bot))


@bot.tree.command(name = "help", description = "Bot Help Command")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Help Command", description="Use .help <command> For Extended Information on a Command.", color=0xE52121)
    embed.add_field(name="Member Command👥", value="avatar,userinfo,serverinfo,stats,afk")
    embed.add_field(name="Admin Command👮", value="kick,ban,unban,giverole,warn,slowmode,say")
    
    embed.set_footer(text=f"Requested By - {interaction.user.name}", icon_url=interaction.user.avatar)
    
    
    await interaction.response.send_message(embed=embed)

@bot.command()
async def userinfo(ctx, user: discord.Member=None):

    if user==None:
        user=ctx.author
    
    rlist = []
    for role in user.roles:
        if role.name != "@everyone":
            rlist.append(role.mention)
    
    b = ", ".join(rlist)

    embed = discord.Embed(color=0xE52121, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.display_avatar),
    embed.set_footer(text=f"Requested By - {ctx.author}",
    icon_url=ctx.author.display_avatar)

    embed.add_field(name='ID:', value=user.id, inline=False)
    embed.add_field(name="Name:", value=user.display_name, inline=False)

    embed.add_field(name="Created at:", value=discord.utils.format_dt(user.created_at), inline=False)
    embed.add_field(name="Joined at:", value=discord.utils.format_dt(user.joined_at), inline=False)


    embed.add_field(name="Bot?", value=user.bot, inline=False)

    embed.add_field(name=f"Roles:({len(rlist)})", value=''.join({b}),inline=False)
    embed.add_field(name="Top Role:", value=user.top_role.mention, inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def stats(ctx: commands.Context):
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
        
    embed = discord.Embed(title="Pong!", description=f"💡 Status: **Ready** \n"
    "📡 Bot Latancy: \n"
    f"<:emoji3:1056289442056384553>  **{round(bot.latency * 1000)}ms**", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="🏰 Servers:", value=servers, inline=True)
    embed.add_field(name="👥 Members:", value=members, inline=True)
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/867345989216108564/1056302275561263175/emoji.png")
    await ctx.send(embed=embed)
    
@bot.command()
async def serverinfo(ctx):
 owner=ctx.guild.owner_id
 embed = discord.Embed(title="Server information", color=0xE52121, timestamp=ctx.message.created_at)
 embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
 embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
 embed.add_field(name="Server Owner", value=f'<@{owner}>', inline=True)
 embed.add_field(name="Text Channels", value=len(ctx.message.guild.text_channels), inline=True)
 embed.add_field(name="Voice Channels", value=len(ctx.message.guild.voice_channels), inline=True)
 embed.add_field(name="Stage Channel", value=len(ctx.message.guild.stage_channels))
 embed.add_field(name="Categories", value=len(ctx.message.guild.categories), inline=True)
 embed.add_field(name="Roles", value=len(ctx.message.guild.roles), inline=True)
 embed.add_field(name="ServerBooster", value=ctx.guild.premium_subscription_count, inline=True)
 embed.add_field(name="CreatedAt", value=discord.utils.format_dt(ctx.guild.created_at))
 embed.set_footer(text=f"Requested By - {ctx.author}",
 icon_url=ctx.author.display_avatar)
 await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)

async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = "None"):
    Ownembed = discord.Embed(title=f"User Kicked", description=f"**Kicked User Name** : `{member.display_name}`\n"
    f"**kicked By** : `{ctx.author.display_name}`\n"
    f"**Reason** : `{reason}`", color=0xE52121, timestamp=ctx.message.created_at)
    Ownembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/867345989216108564/1051937860372140114/emoji.png")
    Ownembed.set_footer(text=f"Requested By {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await member.kick(reason=reason)
    await ctx.send(embed=Ownembed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx: commands.Context, member: discord.Member, role: discord.Role):

    ey = discord.Embed(title="Successfuly Gived Role✔", description=f"**Gived Role To** : `{member.display_name}`\n"
    f"**Modrator** : `{ctx.author.display_name}`", color=0xE52121, timestamp=ctx.message.created_at)
    ey.set_thumbnail(url="https://cdn.discordapp.com/attachments/867345989216108564/1051939765815083120/emoji.png")
    ey.set_footer(text=f"Requested By {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await member.add_roles(role)
    await ctx.send(embed=ey)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = "None"):
    await member.ban(reason=reason)
    Ownbed = discord.Embed(title=f"User Banned✈", description=f"**Banned User Name** : `{member.display_name}`\n"
    f"**Banned By** : `{ctx.author.display_name}`\n"
    f"**Reason** : `{reason}`", color=0xE52121, timestamp=ctx.message.created_at)
    Ownbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/867345989216108564/1051939022622171186/emoji.png")
    Ownbed.set_footer(text=f"Requested By {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.send(embed=Ownbed)

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx: commands.Context, *, to_say):
    await ctx.send(to_say)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx: commands.Context, id: int):
    member = discord.Member
    reason: str = "None"
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    ey = discord.Embed(title=f"User Banned✈", description=f"**Banned User Name** : `{member.display_name}`\n"
    f"**Banned By** : `{ctx.author.display_name}`\n"
    f"**Reason** : `{reason}`", color=0xE52121, timestamp=ctx.message.created_at)
    ey.set_thumbnail(url="https://cdn.discordapp.com/attachments/867345989216108564/1051941730431287316/emoji.png")
    ey.set_footer(text=f"Requested By {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.send(embed=ey)
    

@bot.command()
async def avatar(ctx:commands.Context, avamember: discord.Member = None):
    if avamember == None:
        embed = discord.Embed(description='❌ Error! Please specify a user',
                                  color=discord.Color.red())
        await ctx.reply(embed=embed, mention_author=False)
    else:
        embed = discord.Embed(title=('{}\'s Avatar'.format(avamember.name)), timestamp=ctx.message.created_at, colour=discord.Colour.red())
        embed.set_image(url='{}'.format(avamember.display_avatar))
        embed.set_footer(text=f"Requested By {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
        await ctx.reply(embed=embed, mention_author=False)



@bot.event
async def on_ready():
    print('Bot is ready')

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'🏰{servers} Servers And 👥{members} Members'
    ))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member, *, reason: str):
    
    embed = discord.Embed(title=f"You Received Warn From {ctx.guild.name}", timestamp=ctx.message.created_at, color=0xE52121)
    embed.add_field(name="**Modrator:**", value=f"{ctx.author.name}")
    embed.add_field(name="**Warned:**", value=f"{user.name}")
    embed.add_field(name="**Reason:**", value=f"{reason}")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    ey = discord.Embed(title="Warned Succsesfully")
    ey = discord.Embed(title=f"You Received Warn From {ctx.guild.name}", timestamp=ctx.message.created_at, color=0xE52121)
    ey.add_field(name="**Modrator:**", value=f"{ctx.author.name}")
    ey.add_field(name="**Warned:**", value=f"{user.name}")
    ey.add_field(name="**Reason:**", value=f"{reason}")
    ey.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await user.send(embed=embed)
    await ctx.send(embed=ey)
    
    
@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, time_str: str):

    """Enables slowmode in the current channel"""
    time_regex = re.compile(r'^(\d+)([smh])$')
    match = time_regex.match(time_str)

    if not match:
        await ctx.send('Invalid time format. Use [number][s/m/h] (e.g. 10s, 5m, 2h).')
        return

    time = int(match.group(1))
    unit = match.group(2)

    if unit == 's':
        delay = time
    elif unit == 'm':
        delay = time * 60
    elif unit == 'h':
        delay = time * 60 * 60
    else:
        await ctx.send('Invalid time unit. Use s for seconds, m for minutes, or h for hours.')
        return

    await ctx.channel.edit(slowmode_delay=delay)
    await ctx.send(f"✅ Slowmode enabled for {time_str} in this channel.")
    


afk_dict = {}

@bot.event
async def on_message(message):


    embed1 = discord.Embed(title="AFK Unlocked🔓", description=f"Welcome Back {message.author.mention}! You Are No Longer AFK.", color=0x81d860, timestamp=message.created_at)

    if message.author == bot.user:
        return

    if message.author in afk_dict:
        await message.channel.send(embed=embed1)
        afk_dict.pop(message.author)
        try:
            await message.author.edit(nick=message.author.display_name.replace('(AFK)', ''))
        except discord.Forbidden:
            pass

    
  
    for member in message.mentions:
        if member in afk_dict:
            await message.channel.send(f'{member.name} is currently AFK. For Reason : {afk_dict[member]}')

    await bot.process_commands(message)

@bot.command()
async def afk(ctx, *, reason=None):
    embed3 = discord.Embed(title="AFK Enabled🔒", description="You Sucsesfully Enabled AFK", color=0xE52121, timestamp=ctx.message.created_at)
    embed3.add_field(name="Reason: ", value=reason)
    embed3.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    if reason is None:
        reason = 'No reason provided'
    afk_dict[ctx.author] = reason
    await ctx.reply(embed=embed3)
    try:
        await ctx.author.edit(nick=f'(AFK){ctx.author.display_name}')
    except discord.Forbidden:
        pass
    
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Help Command", description="Use .help <command> For Extended Information on a Command.", color=0xE52121)
    embed.add_field(name="Member Command👥", value="avatar,userinfo,serverinfo,stats,afk")
    embed.add_field(name="Admin Command👮", value="kick,ban,unban,giverole,warn,slowmode,say")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)


    await ctx.reply(embed=embed)


@help.command()
async def avatar(ctx):
    embed = discord.Embed(title="Avatar🖼️", description="See Member Avatar", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".avatar <Member>")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)


@help.command()
async def userinfo(ctx):
    embed = discord.Embed(title="UserInfo", description="See Your Info Or Member Info In Server", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".userinfo <member>")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="ServerInfo", description="Show Server Info", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".serverinfo")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def stats(ctx):
    embed = discord.Embed(title="Stats📡", description="Show Ping And Count Server And Count Member", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".stats")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def afk(ctx):
    embed = discord.Embed(title="AFK🔒", description="Evreyone Know You Are AFK", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".afk [Reason]")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def kick(ctx):
    embed = discord.Embed(title="Kick", description="Kick Member From Server", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".kick <member> [Reason]")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def ban(ctx):
    embed = discord.Embed(title="Ban", description="Ban Member From Server", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".ban <member> [Reason]")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def unban(ctx):
    embed = discord.Embed(title="UnBan", description="UnBan Member From Server", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".unban <member id> [Reason]")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def giverole(ctx):
    embed = discord.Embed(title="GiveRole", description="Give Role To Member", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".giverole <member> <Role Mention & Role Id>")
    await ctx.reply(embed=embed)

@help.command()
async def warn(ctx):
    embed = discord.Embed(title="Warn", description="Warn To Member", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".warn <member> [Reason]")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

@help.command()
async def slowmode(ctx):
    embed = discord.Embed(title="SlowMode", description="Set Slow Mode To Channel", color=0xE52121, timestamp=ctx.message.created_at)
    embed.add_field(name="**Syntax**", value=".slowmode [number][s/m/h]")
    embed.set_footer(text=f"Requested By - {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
    await ctx.reply(embed=embed)

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Member not found.")
    else:
        await ctx.send("An Error Occurred.")


bot.run(os.environ["DISCORD_TOKEN"])
