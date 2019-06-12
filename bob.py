import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import *
import youtube_dl
import requests
import time
import sys
import datetime
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
prefix = ("~" , "#")
Hideout = commands.Bot(command_prefix= prefix)
Hideout.remove_command('help')
token = ""
@Hideout.event
async def  on_ready():
    print("Bot is online")


@Hideout.command(aliases=['coin'])
async def bitcoin(ctx):
    discord_webhook_url = 'https://discordapp.com/api/webhooks/578860275512377344/1zSL4Xd5X7uUPzJa-yemMMNFgPevH-LwJa3Btwz9HcYbd4YQZ4s5zJTeurOa8HND-eGg'

# Get the BTC price from CoinDesk
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate']

# Post the message to the Discord webhook
    data = {
    "content": "Bitcoin price is currently at $" + price_in_usd + " USD"
    }
    requests.post(discord_webhook_url, data=data)

#@Hideout.command(aliases=["ynews" , "news"])
#async def Yahoo_News(ctx):

@Hideout.command(aliases=["info"])
async def userinfo(ctx , member : discord.Member):
    author = ctx.message.author
    cmnd = ctx.message.content
    await ctx.send(f"User {author} had tried to do the following command {cmnd}")
    embed = discord.Embed(title="Hidout Management" , description="Thank you for using Hideout Radio")
    #embed.set_thumbmail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}')
    embed.add_field(name="ID of member:", value=member.id)
    embed.add_field(name="Member that requests information:", value=member.display_name)
    embed.add_field(name="Created at:" , value=member.created_at.strftime("%a, %#d %B %Y, %I:M %p UTC "))
    embed.add_field(name="Joined at:" , value=member.joined_at.strftime("%a, %#d %B %Y, %I:M %p UTC "))
    embed.add_field(name="Top Roles:", value=member.top_role.mention)
    embed.add_field(name="Is it a Bot?" , value=member.bot)
    embed.add_field(name="Avatar: " , value=member.avatar_url)
    await ctx.send(embed=embed)

@Hideout.command(aliases=["er"])
async def Emergency(ctx , member : discord.Member):
        embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
        embed.add_field(name=f"{ctx.message.author}" , value=f"**DEFCON 1 INITIATED**")
        embed.add_field(name=f"Are you sure you want to proceed{ctx.author}? This is a dangerous function!" , value="*More coming soon*")
        embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
        embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
        await ctx.send(embed=embed)
        #await ctx.guild.mute(member)
@Hideout.command(aliases=["destroy" , "kill"])
async def Security(ctx , member : discord.Member):
    await ctx.send("**STAGE ONE COMPLETED ADMIN COMMAND ONLY**")
    await ctx.message.channel.set_permissions(member, read_messages=False, send_messages=False)
    await ctx.send("**ALL CHANNELS LOCKED**")
    embed = discord.Embed(title="The Destroyer" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"{ctx.message.author.mention}" , value=f"**DEFCON 1 INITIATED**")
    embed.add_field(name=f"**YOU WERE WARNED AND DECIDED TO BREAK THE RULES!**" , value="*LOCKING USER*")
    embed.add_field(name=f"Mobile Status {member.mobile_status}" , value=f"*WEB STATUS{member.web_status}* | **GATHERING TOKEN(In Dev)**")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await ctx.send(embed=embed)
@Hideout.command( aliases=["ban"])
async def ban_member(ctx , member : discord.Member ):
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"{ctx.message.author}" , value=f"Banning member below")
    embed.add_field(name=f"Member requested management {ctx.author}" , value="*More coming soon*")
    embed.add_field(name=f"Member banned: " , value=f"{member.name}")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await  ctx.guild.ban(member)
    await  ctx.send(embed=embed)
@Hideout.command(aliases=["mute" , "shut"])
async def Mute_member(ctx , member : discord.Member):
    author = ctx.message.author
    cmnd = ctx.message.content
    await ctx.send(f"User {author} had tried to do the following command {cmnd}")
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"{ctx.message.author}" , value=f"*More features coming**")
    embed.add_field(name=f"Muting the member selected" , value="*More coming soon*")
    #embed.add_field(name=f"Member banned: " , value=f"**More coming**") member.name
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    #await ctx.guild.mute(member)
    await ctx.send(embed=embed)
@Hideout.command()
async def kick(ctx , member : discord.Member  , * , reason=None):
    author = ctx.message.author
    cmnd = ctx.message.content
    await ctx.send(f"User {author} had tried to do the following command {cmnd}")
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"{ctx.message.author}" , value=f"Kicking member below")
    embed.add_field(name=f"Member requested management {ctx.author}" , value="*More coming soon*")
    embed.add_field(name=f"Member kicked: " , value=f"{member.name}")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await  member.kick(reason=reason)
    await  ctx.send(embed=embed)
@Hideout.command()
async def ping(ctx):
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"**NETWORK MANAGEMENT**" , value="*More coming soon*")
    embed.add_field(name=f"*Ping:* " , value=f"{round(Hideout.latency * 1000)} ms")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await ctx.send(embed=embed)
@Hideout.command(aliases=["nick"])
async def nickname(ctx ,member : discord.Member):
    author = ctx.message.author
    cmnd = ctx.message.content
    await ctx.send(f"User {author} had tried to do the following command {cmnd}")
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"{ctx.message.author}" , value=f"Nickname of member below")
    embed.add_field(name=f"Member requested management {ctx.author}" , value="*More coming soon*")
    embed.add_field(name=f"Member nickname changed:  " , value=f" {member.nick}")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await ctx.send(embed=embed)
@Hideout.command(aliases=["prune" , "purge" ,"clear"])
async def Clean_server(ctx  ,amount=5):
    await ctx.channel.purge(limit=amount)
#@Hideout.event
#async def on_message_delete(message):
    #fmt = '{0.author} has deleted the message: {0.content}'

#    await message.channel.send(fmt.format(message))


@Hideout.command(aliases=["paper"])
async def game(ctx):
    #await ctx.send("Game is currently in development please wait for the menu to load")
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    #embed.add_field(name=f"Paper" , value=f"📰")
    #embed.add_field(name=f"Rock" , value="Choose carefully! i might throw a rock!")
    #embed.add_field(name=f"Scissors " , value=f"✂️")
    #embed.add_field(name=f"React to the following emojis below in order to pick!" , value=f" This may be buggy so please wait till my developer finishes me :( ")
    embed.add_field(name="**INFORMATION:**" , value="**IN DEVELOPMENT**")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    #emojis = "📰 ✂️"
    #await ctx.message.add_reaction(emojis)
    msg = await ctx.send(embed=embed)
@Hideout.command(aliases=['mcheck'])
async def moderation_check(ctx):
    channel = ctx.message.channel
    entries = await ctx.guild.audit_logs(limit=None, user=ctx.guild.me).flatten()
    await channel.send('I made {} moderation actions.'.format(len(entries)))
@Hideout.command(aliases=["seclogs"])
async def Sec_logs(ctx):
    async for entry in ctx.guild.audit_logs(limit=100):
        await ctx.send('The following user {0.user} did {0.action} to {0.target}'.format(entry))
@Hideout.command(aliases=["chess"])
async def Chess(ctx , choose : str):
    channel = ctx.message.channel
    await ctx.send("Game is currently in development please wait for the menu to load")
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"Army" , value=f"Castle, the basics you idiot! ")
    embed.add_field(name=f"Queen" , value="I will outrank you!")
    embed.add_field(name=f"King " , value=f"The God himself! Type in checkmate to demolish this God!")
    embed.add_field(name=f"React to the following emojis below in order to pick!" , value=f" This may be buggy so please wait till my developer finishes me :( ")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await ctx.send(embed=embed)
    if "castle" in choose:
        await channel.send("I moved my queen! Try again!")
    if "queen" in choose:
        await channel.send("You shall not checkmate me!")
    elif "king" in choose:
        await channel.send("How dare you try to checkmate me! Here is my horse!")
    elif "checkmate" in choose:
        await channel.send("*Dam you!*  *Type in checkmate five times to kill the king!*")
#Below is for moderation
@Hideout.command(aliases=["defcon_2"])
async def Defcon_2(ctx , role : discord.Role):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = False
    channel = ctx.message.channel
    await channel.set_permissions(role, overwrite=overwrite)
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"**SECURITY NOTICE**" , value="You were warned")
    embed.add_field(name=f"*ROLE LOCKED* " , value=f"*The following role {role.name} along the members have been locked!*")
    embed.add_field(name=f"*ROLE ID:*" , value=f"{role.id}")
    embed.add_field(name="**NOTICE:**" ,  value="**DEFCON 1 INITIATED, OWNER AND STAFF NOTIFIED**")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    await ctx.send(embed=embed)
@Hideout.command(aliases=['memb_lock'])
async def lock(ctx , member : discord.Member):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = False
    channel = ctx.message.channel
    member.permissions_in(channel)
    await channel.set_permissions(member, overwrite=overwrite)
    await ctx.send(f"**DEFCON 2 INITIATED** {member.name}")

@Hideout.command(aliases=["move"])
async def MV_member(ctx , * , member : discord.Member):
    channel = ctx.message.channel
    await  member.move_to(channel,  reason="Admin has moved you due to rule breaking!" )
@Hideout.command(aliases=['bk'])
async def back(ctx , member : discord.Member):
    channel = ctx.message.channel
    member.permissions_in(channel)
    await channel.set_permissions(member, overwrite=None)
    await ctx.send(f"User can now read and send")
@Hideout.command(aliases=["idle"])
async def id_mood(ctx):
    game = discord.Game("Upgrade/Repair in progress")
    await Hideout.change_presence(status=discord.Status.do_not_disturb, activity=game)
@Hideout.command(aliases=["invite" ,"invites"])
async def Invite_member(ctx):
    channel = ctx.message.channel
    await Hideout.create_invite(max_age=1 , max_uses=20)
    author = ctx.message.author
    cmnd = ctx.message.content
    ctx.send(f"user {author} had tried to do the following command {cmnd}")
    #await channel.send(f"The following is the invite {Iinvite}")
    #await channel.send(f"")
        # invite_embed = discord.Embed(title="Invitation" , description="Your invite is below" , color=0x6d6d6d)
        # invite_embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
        # invite_embed.add_field(name="invite" , value=f"{author} " , inline=True)
        # invite_embed.set_footer(text="Made possible by Cipher Technologies")
        # await ctx.send(embed=invite_embed)
    #except:
    #    author = ctx.message.author
    #    invite_embed = discord.Embed(title="Invitation" , description="Your invite is below" , color=0x6d6d6d)
    #    invite_embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    #    invite_embed.add_field(name="This bot has accountered an error, please contact my developer" , value=f"Error code 5 " , inline=True)
    #    invite_embed.set_footer(text="Made possible by Cipher Technologies")
    #    await ctx.send(embed=invite_embed)

@Hideout.command(aliases=["site_scan" , "scan"])
async def scanner(ctx , link : str):
    _get_request = requests.get(format(link))
    await ctx.send(f"Results of the website crawler and/or scanner {_get_request} RETURNS 200 IF ONLINE")
    #await ctx.send(f"Content of the site {_get_request.content}")
    embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
    embed.add_field(name=f"Status Code" , value=f"{_get_request.status_code}")
    embed.add_field(name=f"Scanner" , value="Below is the header of the website")
    embed.add_field(name=f"NOTICE" , value=f"Please note I am not responsible for your actions if this is misused! ")
    embed.set_footer(text="Please note this Bot is copyrighted under GPLV4 Soon to be Commerical lincesed.")
    embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    time.sleep(20)
    msg = await ctx.send(embed=embed)
    await ctx.send(f"The header:\n {_get_request.headers}")
    if _get_request.status_code == 502:
        embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
        embed.add_field(name=f"Status Code" , value=f"{_get_request.status_code}")
        embed.add_field(name=f"The following site has blocked access" , value=f"{_get_request.status_code}")
        ctx.send(embed=embed)

@Hideout.command(aliases=["Hideout" , "hide"])
async def hideout_game(ctx):
        await ctx.send("Game is currently in development")
        embed = discord.Embed(title="Hidout Radio" , description="Thank you for using Hideout Radio")
        embed.add_field(name=f"Weapons" , value=f"⚔")
        embed.add_field(name=f"Armory" , value="Choose what  you wish for if i have in supply!")
        embed.add_field(name=f"Gangs " , value=f"🕵")
        embed.add_field(name=f"Enemies" , value="Cautious! You never know what you are getting into!")
        embed.add_field(name=f"Big Brother" , value="👁‍🗨 Is watching your moves! Counter this by reacting to the game!")
        embed.add_field(name=f"React to the following emojis below to play the game or enter 'Hideout' below!" , value=f" This official game is licenced under MIT")
        embed.set_footer(text="Please note this Bot is copyrighted under MIT  Soon to be Commerical lincesed.")
        embed.set_author(name=Hideout.user.name , icon_url=Hideout.user.avatar_url)
    #    emojis = "📰 ✂️"
    #    await ctx.message.add_reaction(emojis)
        msg = await ctx.send(embed=embed)

@Hideout.command(aliases=['conn' , 'connect' , 'join'])
async def Join(ctx , *  , vc : discord.VoiceClient):
    await Hideout.connect(vc)
@Hideout.command(aliases=["help"])
async def Help_user(ctx):
    try:
         author = ctx.message.author
         help_embed = discord.Embed(title="Help menu" , description="Welcome to the help menu" , color=0x6d6d6d)
         help_embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
         help_embed.add_field(name="help" , value="Shows this message in private messaging and in channels" , inline=True)
         help_embed.add_field(name="invite" , value="Create's invites " , inline=True)
         help_embed.add_field(name="prg/prune" , value="Prunes an amount of messages", inline=True)
         help_embed.add_field(name="sc" , value="(Admin command only)Locks all channels and stops server raiding" , inline=True)
         help_embed.add_field(name="play" , value="Plays music and/or YouTube videos (Audio only)" , inline=True)
         help_embed.add_field(name="disconnect", value="disconnects from voice channel" , inline=True)
         help_embed.add_field(name="ban" , value="Command not available at the moment but bans member" , inline=True)
         help_embed.add_field(name="kick" , value="Kicks a member (all ban and kick commands are used by admins only)", inline=True)
         help_embed.add_field(name="pause" , value="Pauses the audio/video" , inline=True)
         help_embed.add_field(name="stop" , value="Stops audio/video " , inline=True)
         help_embed.add_field(name="wordf", value="Shows all currently forbidden words and member that cursed using these words", inline=True)
         help_embed.set_footer(text="Made possible by Cipher Technologies")
         await ctx.send(author , embed=help_embed)
    except:
        await Breakouts.say("**Cannot show help menu at the moment, please try again later**")




















Hideout.run(token)
