import discord
from discord.ext.commands import Bot
import logging
import asyncio
from itertools import cycle
import random
import youtube_dl
import requests
from datetime import *
from steam import *
from steam import SteamClient
from steam.enums.emsg import EMsg
import socket
prefix_value = ("sec" , "??", ".")
Breakouts = Bot(command_prefix=prefix_value)
Breakouts.remove_command('help')
token = "YOUR TOKEN"
players_update = {}
server = discord.Server(id='YOUR SERVER ID')
players= {}
queues = {}
def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@Breakouts.event
async def  on_ready():
    print("Bot is online")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

 #Below are commands that dow the following listed below:

 #Security notice, Warns administartors and Owner.
@Breakouts.event
async def on_group_join(channel, user):
    security_log = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"The following user {user}is in the following group call/channel{channel}")
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
@Breakouts.event
async def on_typing(channel, user, when):
    log_channel = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="User Data", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.set_thumbnail(url="https://image.ibb.co/bGrhzp/breakoutservers_logo.jpg")
    embed.add_field(name=f"**USER DATA  NOTICE  USER TYPING TIME :warning:** ", value=f"{when}", inline=True)
    embed.add_field(name=f"**USER DATA  NOTICE  USER TYPING TIME WITHIN CHANNEL :warning:** ", value=f"{channel}", inline=True)
    embed.add_field(name=f"**USER DATA  NOTICE  USERNAME TYPING WITHIN THE TIME :warning:** ", value=f"{user}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(log_channel , embed=embed)
    #geo = pygeoip.GeoIP("/usr/share/GeoIP/GeoIP.dat")
   # await Breakouts.say(f"Using {geo} , in development, my apologies, IP logging will be later available" , log_channel)
  #  for giy in geo:
     #   giy.country_name_by_addr(geo)
     #   print(giy)
@Breakouts.event
async def on_member_update(before, after):

    log_channel = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"status:" , value=f" {before.status} was the status of the member {before} " )
    embed.add_field(name=f"status:" , value=f" {after.status} is now the status {after}" )
    embed.add_field(name=f"Game Information:" , value=f"was playing {before.game}" )
    embed.add_field(name=f"Game Information:" , value=f"is now the game playing {after.game}" )
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(log_channel ,embed=embed)
@Breakouts.event
async def on_server_role_create(role):
    security_log = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE ROLE CREATED** ", value=f"{role}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(security_log , embed=embed)
@Breakouts.event
async def on_reaction_add(reaction, user):
    log_channel = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE REACTION ADDED** ", value=f" The the following reaction {reaction} was given  by this user:\t{user}  **YOU ARE BEING WATCHED**", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_typing(log_channel)
    await Breakouts.send_message(log_channel , embed=embed)
@Breakouts.event
async def on_group_join(channel, user):
    log_channel = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE USER JOINED GROUP CALL/CHANNEL** ", value=f" The the following user joined a channel and/or group call{user} within {channel}:\t  **YOU ARE BEING WATCHED**", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_typing(log_channel)
    await Breakouts.send_message(log_channel , embed=embed)
@Breakouts.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** RAW MESSAGE METADATA:\n{1.content}'

    #if Breakouts.user:
    #    pass

    embed=discord.Embed(title="Messages edited", description="Server logging and security management")
    embed.add_field(name=f"edited Message below", value="Reason: Change of mind or  hiding something" , inline=True)
    embed.add_field(name=f"edited Message: ", value=f"Message: {fmt.format(before , after)}" , inline=True)
    await Breakouts.send_message( Breakouts.get_channel(id='564953938160254996') , "*My apologies for the spam, i just need to log for your safety*" )
    asyncio.sleep(40)
@Breakouts.event
async def on_server_role_update(before, after):
    security_log = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE ROLE CREATED** ", value=f" The following role was updated:{before} and the updated version: {after}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(security_log , embed=embed)
@Breakouts.event
async def  on_server_role_delete(role):
    security_log = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE ROLE DELETED** ", value=f"{role}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(security_log ,  embed=embed)
@Breakouts.event
async def on_group_remove(channel, user):
    log_channel = Breakouts.get_channel("564953938160254996")
    await Breakouts.say( log_channel, f"**The following member: {user} is in the corresponding channel: {channel}**")
@Breakouts.event
async def on_member_ban(member):
    log_channel = Breakouts.get_channel("564953938160254996")
    await Breakouts.send_message( log_channel, f"**Member banned: {member}**")
@Breakouts.event
async def on_member_unban(server, user):
    log_channel = Breakouts.get_channel("564953938160254996")
    await Breakouts.send_message( log_channel, f"*Member unbanned: {user} from the following server {server}*")
@Breakouts.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    log_channel = Breakouts.get_channel("541548377134071825")
    await Breakouts.send_message(log_channel , "**{} Took down the following message: {}**".format(author , content))
    await Breakouts.process_commands(message)
#not  here
@Breakouts.event
async def on_channel_update(before , after):
    log_channel = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="NOTICE   ", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**INFORMATION: CHANNEL UPDATED :warning:** ", value=f"{after}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(log_channel , embed=embed)
@Breakouts.event
async def on_channel_create(channel):
    security_log = Breakouts.get_channel("564953938160254996")
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE CHANNEL CREATED** ", value=f"{channel}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(security_log ,  embed=embed)
@Breakouts.event
async def server_role_update(before, after):
    security_log = Breakouts.get_channel("564953938160254996")
    await Breakouts.send_message(security_log , f"**ROLE:\t** {before}")
    await Breakouts.send_message(security_log,f"**âš  ROLE UPDATED: {after} âš ")
@Breakouts.event
async def on_member_join(member):
    #work here
    autorole = discord.utils.get(member.server.roles, name='DarkRP')
    await Breakouts.add_roles(member, autorole)
    welcome_user = Breakouts.get_channel(id="564953938160254996")
    #await Breakouts.send_message( welcome_user, '{0} joined on {0.joined_at}'.format(member))
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    Date_today = date.today()
    embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE USER JOINED** ", value=f"{member}", inline=True)
    embed.add_field(name=f"DATE JOINED: {Date_today}" , value=f"{member}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(welcome_user ,  embed=embed)
@Breakouts.event
async def on_server_update(before, after):
    security_log = Breakouts.get_channel("564953938160254996")
    await Breakouts.send_message(security_log , "**SERVER SECURITY NOTICE**: *SERVER UPDATED/MODIFED:*\n")
    await Breakouts.send_message(security_log  , f"{before}")
    await Breakouts.send_message(security_log , "UPDATED VERSION:\n")
    await Breakouts.send_message(security_log, f"{after}")
@Breakouts.event
async def voice_state_update(before, after):
    log_channel = Breakouts.get_channel("564953938160254996")
    await Breakouts.send_message(log_channel , f"{before}")
    await Breakouts.send_message(log_channel, f"{after}")
@Breakouts.event
async def on_member_remove(member):
    log_channel = Breakouts.get_channel("564953938160254996")
    await Breakouts.send_message(log_channel , f"**{member}**" + "Has left the server, ciao!")
@Breakouts.command(pass_context=True)
async def  check_user(ctx , member : discord.Member):
    message = ctx.message.channel
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**SECURITY NOTICE USER DATA** ", value=f"The user is playing:\t{member.game}", inline=True)
    embed.add_field(name=f"OTHER INFORMATION BELOW:\t{member.joined_at}" , value=f"{member}", inline=True)
    embed.add_field(name=f"OTHER INFORMATION BELOW:" ,  value=f"STATUS:\t{member.status}")
    embed.add_field(name=f"OTHER INFORMATION BELOW:" ,  value=f"USER COLOR:\t{member.color}")
    #embed.add_field(name=f"OTHER INFORMATION BELOW:" ,  value=f"ROLES GIVEN:\t{member.roles}")
   # embed.add_field(name=f"OTHER INFORMATION BELOW:" , value=f"SERVER PERMISSIONS:\t{member.server_permissions}")
    embed.add_field(name=f"OTHER INFORMATION BELOW:" ,  value=f"USER NICKNAME:\t{member.nick}")
    embed.add_field(name=f"OTHER INFORMATION BELOW:" ,  value=f"USER TOP ROLE:\t{member.top_role}")
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.say("**:warning: INFORMATION GIVEN, USE CAREFULLY**" , embed=embed)
@Breakouts.command(pass_context=True , aliases=["join" , "join-channel"])
async def join_channel(ctx):
    voice = ctx.message.author.voice_channel
    await Breakouts.join_voice_channel(voice)
    embed=discord.Embed(title="Notice", color=0x6d6d6d)
    Date_today = date.today()
    embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**NOTICE USER JOINED CHANNEL\n{voice}** ", value=f"Please enjoy your time", inline=True)
    embed.add_field(name=f"DATE JOINED CHANNEL: {Date_today}" , value=f"Joining channel", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(ctx.message.channel ,  embed=embed)
@Breakouts.command(pass_context=True , aliases=["play"])
async def play_song(ctx , url):
    server = ctx.message.server
    voice_client = Breakouts.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url , after= lambda: check_queue(server.id))
    players_update[server.id] =  player
    player.start()
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    Date_today = date.today()
    embed.set_author(name="Cipher", url="https://www.instagram.com/parsathedev/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**NOTICE: Playing audio** ", value=f"Playing music", inline=True)
    embed.add_field(name=f"Date playing: {Date_today}" , value=f"{player.title}", inline=True)
    embed.add_field(name=f"Song duration", value=f"{player.duration}", inline=True)
    embed.add_field(name=f"Link of Music Video:" , value=f"{player.url}")
    embed.add_field(name=f"{Date_today} Please enjoy the service! :wink:" , value=f"{player.uploader}")
    embed.add_field(name=f"Date uploaded:" , value=f"{player.upload_date}")
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.send_message(ctx.message.channel,  embed=embed)
    msg = await Breakouts.say("**use the following reactions to read the description of the song**")
    await Breakouts.add_reaction(msg, '\U0001F3B5')
    descrp =discord.Embed(title="Information", color=0x6d5d6d)
    await Breakouts.wait_for_reaction(emoji=u"\U0001F3B5",  user=ctx.message.author, message=msg)
    descrp.add_field(name=f"**NOTICE: Showing Information of Music Video {player.url}** ", value=f"Likes:\t{player.likes} & dislikes {player.dislikes}", inline=True)
    descrp.add_field(name=f"Date of execution: {Date_today}", value=f"{player.description}",inline=True)
    descrp.add_field(name=f"Thank you for using Breakout Security 0.7.8", value=f"Enjoy the music!", inline=True)
    descrp.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.say(ctx.message.channel ,embed=descrp)
@Breakouts.command(pass_context=True , aliases=['pause'])
async def pause_on_user(ctx):
    servid = ctx.message.server.id
    msg = await Breakouts.say("**use the given reaction to pause the song**")
    await Breakouts.add_reaction(msg, '\U0001F3B5')
    descrp =discord.Embed(title="Information", color=0x6d5d6d)
    descrp.add_field(name=f"Thank you for using  Motion", value=f"Please enjoy the service", inline=True)
    descrp.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.say(ctx.message.channel ,embed=descrp)
    await Breakouts.wait_for_reaction(emoji=u"\U0001F3B5",  user=ctx.message.author, message=msg)
    players_update[servid].pause()
    await Breakouts.say("**Player paused**")
#@Breakouts.command(pass_context=True)
#async def bass(ctx)
@Breakouts.command(pass_context=True , aliases=['stop'])
async def stop_song(ctx):
        servid = ctx.message.server.id
        message = ctx.message.author
        msg = await Breakouts.say("**use the given reaction to stop the song**")
        await Breakouts.add_reaction(msg, '\U0001F3B5')
        descrp =discord.Embed(title="Information", color=0x6d5d6d)
        descrp.add_field(name=f"Thank you for using  Motion", value=f"Thank you for using our service", inline=True)
        descrp.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
        await Breakouts.say(ctx.message.channel ,embed=descrp)
        await Breakouts.wait_for_reaction(emoji=u"\U0001F3B5",  user=ctx.message.author, message=msg)
        #react =await Breakouts.wait_for_reaction([':pause_button:',':play_pause:'], message=":pause_button:")
        embed=discord.Embed(title="Security", color=0x6d6d6d)
        Date_today = date.today()
        embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
        embed.add_field(name=f"**NOTICE: Playing audio** ", value=f"Playing music", inline=True)
        embed.add_field(name=f"Date played: {Date_today}", value=f"Enjoy the music",inline=True)
        embed.add_field(name=f"Stopping song", value=f"Song Stopped", inline=True)
        embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
        msg = await Breakouts.send_message(ctx.message.channel,  embed=embed)
        players_update[servid].stop()

@Breakouts.command(pass_context=True , aliases=['steam_id'])
async def get_steam_id(ctx , link : str):
    st = SteamID.from_url(link)
    await Breakouts.say(f"{st} is the person's SteamID")
    gr = SteamID("76561198059186780")
    group = SteamID("[g:1:0]")
    print(gr.as_steam2)
    await Breakouts.say(f"*{group.community_url} is the community group URL*")

@Breakouts.command(pass_context=True , aliases=['resume' , 'unpause'])
async def resume_on_user(ctx):
    servid = ctx.message.server.id
    msg = await Breakouts.say("**use the given reaction to resume the song**")
    await Breakouts.add_reaction(msg, '\U0001F3B5')
    descrp =discord.Embed(title="Information", color=0x6d5d6d)
    descrp.add_field(name=f"Thank you for using  Motion", value=f"Please enjoy the service", inline=True)
    descrp.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.say(ctx.message.channel ,embed=descrp)
    await Breakouts.wait_for_reaction(emoji=u"\U0001F3B5",  user=ctx.message.author, message=msg)
    players_update[servid].resume()
@Breakouts.command(pass_context=True , aliases=['playing'])
async def is_playing(ctx):
    servid = ctx.message.server.id
    sh = players_update[servid].is_playing()
    #work here
@Breakouts.command(pass_context=True , aliases=['show_error' , 'error'])
async def Show_error(ctx):
    servid = ctx.message.server.id
    err_log = players_update[servid].error
    await Breakouts.say(err_log)
@Breakouts.command(pass_context=True , aliases=["volume"])
async def  near_end(ctx , value : int):
    servid = ctx.message.server.id
    #fin_en = players_update[servid].is_done()
    pl_vol = players_update[servid].volume = value / 100
    await Breakouts.say(f"Volume:\t {value}\n Enjoy the new update!")
    if players_update[servid].is_playing():
        await Breakouts.say("**The volume has been modified**")
        #state =  players.get_voice_state(ctx.message.server)
        #player = state.player
        #work here more  if voice_channel == None:
            #voice_channel = author.voice_channel
@Breakouts.command(pass_context=True , aliases=['defcon2'])
async def Defcon_2(ctx, role : discord.Role):
    server = discord.Server(id='541468834473836566')
   # gt_bans = await Breakouts.replace_roles(member , "Member" , "Moderator" , "Founder")
    #await Breakouts.say(gt_bans + "**ROLES REPLACED FOR SECURITY PURPOSES**")
    if "553129176043880458" or "546331545259212800"    in [role.id for role in ctx.message.author.roles]:
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = False
        overwrite.ban_members = False
        await Breakouts.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await Breakouts.say(f"**CHANNEL OVERRIDED, READING MESSAGES DISABLED** STAGE 3 BEGINNING ")
    else:
        await Breakouts.say("*First warning, do not attempt to use admin commands*")

@Breakouts.command(pass_context=True , aliases=["back"])
async def Rev_action(ctx, role : discord.Role):
    server = discord.Server(id='541468834473836566')
   # gt_bans = await Breakouts.replace_roles(member , "Member" , "Moderator" , "Founder")
    #await Breakouts.say(gt_bans + "**ROLES REPLACED FOR SECURITY PURPOSES**")
    if "553129176043880458" or "546331545259212800"   in [role.id for role in ctx.message.author.roles]:
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = True
        overwrite.ban_members = False
        await Breakouts.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await Breakouts.say(f"**CHANNEL OVERRIDED, SENDING AND  READING MESSAGES  ENABLED** HAULTING TILL FURTHER NOTICE ")
    else:
        await Breakouts.say("*First warning, do not attempt to use admin commands*")
#async def Get_all_messages( ctx ,channel):
   # async for  mess in Breakouts.logs_from(channel):
       #print(mess.clean_content)
@Breakouts.command(pass_context=True , aliases=['ns'])
async def queue(ctx , url):
    server = ctx.message.server
    voice_client = Breakouts.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url , after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await Breakouts.say("Music queued.")

@Breakouts.command(pass_context=True , aliases=['information' , 'getuser' , 'breakout'])
async def user_info(ctx , user : discord.Member):
    inf =await Breakouts.application_info()
    server = discord.Server(id='541468834473836566')
    await Breakouts.say("**Your information below: \n**")
    await Breakouts.say(f"{server.get_member(user)} Stage one")
    await Breakouts.say("**Stage two completed**")
#Work here
@Breakouts.command(pass_context=True , aliases=['avatar',  'av' , 'image'])
async def Get_Avatar(ctx , Iusr : discord.User):
    await Breakouts.say("Below are the requested Image URL of the targeted user.")
    embed=discord.Embed(title="Security", description="User Image")
    embed.set_author(name=f"{ctx.message.author}")
    embed.add_field(name="name of requester", value=f"{ctx.message.author.mention}" , inline=True)
    #embed.add_field(name="Security ", value="Reverse Engineering the Python application is now more difficult with PyCrypto" , inline=True)
#    embed.add_field(name="Audio Issues", value="Bass and Trebble adjusted for a temporary amount of time(depends on your network bandwidth" , inline=True)
    embed.add_field(name="Image", value=f"{Iusr.avatar_url}", inline=True)
    await Breakouts.say(embed=embed)
@Breakouts.command(pass_context=True , aliases=['grp'])
async def Group_call(ctx , gr : str):
    server = ctx.message.server
    message = ctx.message.channel
    group = discord.GroupCall(call=gr)
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    Date_today = date.today()
    embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**NOTICE: Showing group call information** ", value=f"User's in group call{group.connected}", inline=True)
    embed.add_field(name=f"Date displayed and information (IN BETA): {Date_today}" , value=f"{group.call}", inline=True)
    embed.add_field(name=f"Additional Information: ", value=f"coming soon!", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.say(ctx.message.channel , embed=embed)
@Breakouts.command(pass_context=True)
async def Get_call(ctx):
    server = ctx.message.server
    await Breakouts.say("**in development!**")
    vcs =Breakouts.voice_client_in(server)
    await Breakouts.say(f"{vcs}")
  #  Breakouts.group_call_in(vcs)
@Breakouts.command(pass_context=True)
async def Denial(ctx):
    await Breakouts.say("**Whom do you wish to test a Denial Of Service Attack? Please note My author will get your IPs if done illegelly!**")
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    print("Enter IP:\n")
    await Breakouts.say("**ENTER IP: SECURITY COMMAND ONLY**")
    #PORT = [22 , 53 , 21 , 80 , 443]
    PORT =  input()
    IP = input()
    for i in range(1,6663):
        i =   sock.connect_ex((IP , PORT))
    return i
    sock.close()

@Breakouts.command(pass_context=True , aliases=['msg_check'])
async def check_message(ctx , message : discord.Message):
    await Breakouts.say("**Which message do you wish for me to inspect and report?**")
    cont = message.content
    await Breakouts.say(f"{ctx.message.author} is the author of the message {cont}")
@Breakouts.command(pass_context=True)
async def GroupC(ctx , membs : discord.Member):

    if Breakouts.user:
        await Breakouts.say("**Please wait..**")

@Breakouts.command(pass_context=True , aliases=[ "disconnect" , 'leave'])
async def leave_channel(ctx):
    server =  ctx.message.server
    leave =  Breakouts.voice_client_in(server)
    await leave.disconnect()
@Breakouts.command(pass_context=True , aliases=['defcon_3'])
async def emergency_resp( ctx , member : discord.Member):

    #await Breakouts.pin_message(f"**DEFCON 3 INITIATED, MEMBER LOCKED**")
    overwrite = discord.PermissionOverwrite()
    overwrite.read_messages = False
    overwrite.ban_members = False
    await Breakouts.edit_channel_permissions(ctx.message.channel, ctx.message.author.mention, overwrite)

@Breakouts.command(pass_context=True , aliases=['create_channel'])
async def create_channels(ctx):
    if "553129176043880458" or "546331545259212800"     in [role.id for role in ctx.message.author.roles]:
        server = discord.Server(id='541468834473836566')
        await Breakouts.create_channel(server, 'Change Name', type=discord.ChannelType.voice)
        await Breakouts.say("**CHANNEL CREATED :new_moon_with_face: **")
    else:
        await Breakouts.say("*Administrators only command*")
@Breakouts.command(pass_context=True , aliases=['lookup'])
async def get_member_lookup(ctx ,  member : discord.Member):
    server = discord.Server(id='541468834473836566')
   # server.splash_url("")
    server.get_member(member)
    await Breakouts.say(f"{member} Is in the server, else returns None")

@Breakouts.command(pass_context=True , aliases=['info'])
async def bot_information(ctx , msgType : discord.MessageType):
    embed=discord.Embed(title="Security", color=0x6d6d6d)
    Date_today = date.today()
    embed.set_author(name="Cipher", url="https://www.instagram.com/crypt_pas74/" , icon_url="https://cdn.pixabay.com/photo/2017/02/18/12/36/hacker-2077138_960_720.jpg")
    embed.add_field(name=f"**NOTICE: Showing message information** ", value=f"{msgType.default}", inline=True)
    embed.add_field(name=f"User added to private group call within time: {Date_today}", value=f"{msgType.recipient_add}",inline=True)
    embed.add_field(name=f"User removed from private group call: ", value=f"{msgType.recipient_remove}", inline=True)
    embed.add_field(name=f"Group Call Status ", value=f"{msgType.call}", inline=True)
    embed.set_footer(text="ACT 1968 ALL RIGHTS RESERVED ~CIPHER/crypt_pas74 ALL SOURCE CODE ARE PROTECTED UNDER THIS ACT AND AS SUCH  ILLEGAL ACTIONS WILL BE PROSTITUTED IN COURT")
    await Breakouts.say(ctx.message.channel ,embed=embed)

@Breakouts.command(pass_context=True)
async def location(ctx):
    region  = discord.ServerRegion()
    await Breakouts.say(f"{region.sydney} Is the region")
@Breakouts.command(pass_context=True)
async def  game(ctx):
    serv =  ctx.message.server
    msg = await Breakouts.say("*Game being programmed*")
    await Breakouts.edit_message(msg , new_content=f"{ctx.message.author.mention}, game is loading...")
    if "553129176043880458" or "546331545259212800"  in [role.id for role in ctx.message.author.roles]:
        Intro = await Breakouts.say("*Welcome to GTAV Discord Edition*")
        embed=discord.Embed(title="The Destroyer", description="Discord Game")
        embed.set_author(name=f"{ctx.message.author}")
        embed.add_field(name="Attack", value=":crossed_swords:" , inline=True)
        embed.add_field(name="Defense", value=":shield:" , inline=True)
        embed.add_field(name="Economy", value=":moneybag:" , inline=True)
        embed.add_field(name="Weapons", value=":gun:", inline=True)
        await Breakouts.say(embed=embed)
    else:
        await Breakouts.say("*Please assign the Gamer role before playing*")


@Breakouts.command(pass_context=True , aliases=['patch' , 'notes'])
async def Patch_notes(ctx):
    embed=discord.Embed(title="Updates and Security", description="Security Updates")
    embed.set_author(name=f"{ctx.message.author}")
    embed.add_field(name="Issue", value=".lookup Did not work" , inline=True)
    embed.add_field(name="Security update ", value="Reverse Engineering the Python application is now more difficult with PyCrypto" , inline=True)
    embed.add_field(name="Audio Issues", value="Bass and Trebble adjusted for a temporary amount of time(depends on your network bandwidth" , inline=True)
    embed.add_field(name="Server Issues", value="Roles and auto roles are now being patched, should take two weeks to resoleva most.", inline=True)
    await Breakouts.say(embed=embed)

@Breakouts.command(pass_context=True , aliases=['sc'  ,'defcon', 'defcon_1'])
async def request_offline_members(server):
    try:
        if "516173517335691278" or "516167631170961423"   in [role.id for role in ctx.message.author.roles]:
            ge_serv = Breakouts.get_server("541468834473836566")
            await Breakouts.say("** WARNING** FOUNDER AND NETWORK SECURITY ALERTED, DEFCON 1  INITIATED ")
            for server in Breakouts.servers:
                for channel in server.channels:
                    await Breakouts.edit_channel(channel=channel  ,user_limit=10)
            text_channel_list = []
            await Breakouts.say("**READ ONLY MODE INITIALIZED :warning:** ")
            for server_list in Breakouts.servers:
                for channel in server_list.channels:
                    if channel.type ==  discord.ChannelType.text:
                        text_channel_list.append(channel)
                        await Breakouts.say(f"{channel}")
        spammer = ctx.message.mentions[0]
        timeout = time.time() + 60
        shut_channel = await Breakouts.create_channel(ctx.message.server, "Shutdown", type=discord.ChannelType.voice)
        await Breakouts.move_member(spammer , shut_channel)
        await Breakouts.say(f"**DISCORD RAIDER HAULTED UNTIL  {timeout}**")
        overwrite = discord.PermissionOverwrite(server=ge_serv)
        # overwrite.read_messages = False
        # overwrite.ban_members = False
        #  await Breakouts.edit_channel_permissions(channel=gt_channels, target=membs,  overwrite=overwrite)  443375498828185617
    except:

        print("Error")
        #await Breakouts.say(embed = embed)
@Breakouts.command(pass_context=True , aliases=['prune' , 'p'])
async def clear(ctx , amount=100):
    channel  = ctx.message.channel
    messages = []
    try:
        if "553129176043880458" or "546331545259212800"      in [role.id for role in ctx.message.author.roles]:
            async for message in Breakouts.logs_from(channel , limit=int((amount)) + 1):
                messages.append(message)
            await Breakouts.delete_messages(messages)
            pass
        show_msg = await Breakouts.say(':white_check_mark:' + '\t'    + f'**{amount}**' + ' ' + 'messages has been cleared.\t' + ':white_check_mark:', delete_after=1)
            #error here

    except:
        await Breakouts.say("**Couldn't purge messages, my apologies, either try again in 5 minutes or contact my author :warning:  **")
#sets the bot into an idle mood
@Breakouts.command(pass_context=True , aliases=['cls_emoji' , 'emp'])
async def clear_emoji(ctx , reaction : discord.Reaction ,amount=100):
    channel  = ctx.message.channel
    messages = []
  #  try:
    async for message in Breakouts.logs_from(channel , limit=int((amount)) + 1):
        messages.append(message)
    await Breakouts.clear_reactions(messages)
    pass
 #   except Exception as em:
  #      await Breakouts.send_typing(ctx.message.channel)
  #      await Breakouts.say("*An Error has caused me to crash* " + ":speech_balloon:" + str(em))
@Breakouts.command(pass_context=True  , aliases=["set_idle" , "idle"])
async def bid_idle(ctx):
    try:
        await Breakouts.change_presence(game=discord.Game(name="Repaired" , type=3 ,status=discord.Status("idle")))
        print("STATUS CHANGED")
    except:
        await Breakouts.say("An error has occurred my apologies, please report all bugs/glitches to my author crypt_pas74")
@Breakouts.command(pass_context=True , aliases=["set_away", "away"])
async def bid_away(ctx):
    try:
        await Breakouts.change_presence(game=discord.Game(name="Under management" , type=3) ,status=discord.Status("dnd") )
    except:
        print("STATUS CHANGEED TO AWAY")
@Breakouts.command(pass_context=True , aliases=['invite' , 'bid' , 'invitation'])
async def invite_mems(ctx):
    try:
        InvUs  =  await Breakouts.create_invite(ctx.message.channel, xkcd=True)
        await Breakouts.say(InvUs)
    except:
        await Breakouts.say("INVITE FAILED.... " , delete_after=5)
        #here works
@Breakouts.command(pass_context=True , aliases=['nick'])
async def nickname(ctx , member : discord.Member , nick : str):
    try:
        if "553129176043880458" or "546331545259212800"      in [role.id for role in ctx.message.author.roles]:
            content = ctx.message.content
            await Breakouts.change_nickname(member , f"{nick}")
    except:
        await Breakouts.say("**Permission denied!**")
@Breakouts.command(pass_context=True)
async def undo_nick(ctx , member : discord.Member):
    try:
        if "553129176043880458" or "546331545259212800"    in [role.id for role in ctx.message.author.roles]:
            content = ctx.message.content
            await Breakouts.change_nickname(member , None)
    except:
        await Breakouts.say("*Admin command only*")
@Breakouts.command(pass_context=True , aliases=['update'])
async def update_name(ctx):
    change = ctx.message.server.me
    await Breakouts.change_nickname(change , "Breakout Security 0.7.8")
    embed=discord.Embed(title="New name", description="Name Change")
    embed.set_author(name=f"{ctx.message.author}")
    embed.add_field(name="Before", value=" Breakout Security 0.7.4" , inline=True)
    embed.add_field(name="After", value="Breakout 0.7.8" , inline=True)
    embed.add_field(name="Developer", value="Cipher" , inline=True)
    embed.add_field(name="license", value="GPLV3+ Soon Commercial license", inline=True)
    await Breakouts.say(embed=embed)
@Breakouts.command(pass_context=True)
async def kick(ctx , member : discord.Member):
    await Breakouts.kick(member)
    embed=discord.Embed(title="Member Kicked", description="Pruning and server management")
    embed.set_author(name=f"{ctx.message.author}")
    embed.add_field(name=f"Member: {member}", value="Reason soon coming!" , inline=True)
    embed.add_field(name=f"By: {ctx.message.author}", value="Breakout 0.7.4" , inline=True)
@Breakouts.event
async def on_message_edit(before, after):
        fmt = '**{0.author}** RAW MESSAGE METADATA:\n{1.content}'
        #cont = '{1.content}'
      #  auth = '{0.author}'
        #embed=discord.Embed(title="Messages edited", description="Server logging and security management")
        #embed.add_field(name=f"edited Message below", value="Reason: Change of mind or  hiding something" , inline=True)

        await Breakouts.send_message( Breakouts.get_channel(id='541548377134071825') ,  fmt.format(after , before))
        #await Breakouts.send_message( Breakouts.get_channel(id='541434596215095322'), embed=embed)
       # await Breakouts.send_message( Breakouts.get_channel(id='541434596215095322') , fmt.format(after, before))
@Breakouts.event
async def on_message_delete(message):
    wamsg = '{0.content} **I am watching**"'
    await Breakouts.send_message(Breakouts.get_channel(id='541548377134071825') , wamsg.format(message))

@Breakouts.command(pass_context=True , aliases=['moderator' , 'mod'])
async def  add_moderator(ctx , member : discord.Member):
	#add a try except here
    role = discord.utils.get(ctx.member.server.roles, name="Moderator")
    await Breakouts.add_roles(member, role)
    if "553129176043880458" or "546331545259212800"    in [role.id for role in ctx.message.author.roles]:
        await Breakouts.say("**Adding moderator**")

    else:
        await Breakouts.say("**PERMISSION DENIED** :warning:")

@Breakouts.command(pass_context=True , aliases =['status'])
async def Find_Status(ctx , member : discord.Member):
    await Breakouts.say("*Below is the status of the user*")
    embed=discord.Embed(title=f"staff requested {ctx.message.author}", description="Sever Security and user management")
    embed.set_author(name=f"{ctx.message.author}")
    embed.add_field(name=f"Status of the user ", value=f" status {member.status}" , inline=True)
    embed.add_field(name=f"The game playing:", value=f"{member.game}" , inline=True)
    embed.add_field(name="Nickname:" , value=f"{member.nick}")
    embed.add_field(name=f"Joined at:" , value=f"{member.joined_at}")
    embed.add_field(name=f"Color of member:" , value=f"{member.color}")
    await  Breakouts.send_message(ctx.message.channel ,embed=embed)
@Breakouts.command(pass_context=True , aliases=['shut'])
async def mute(ctx , member : discord.Member):
    try:
        if "553129176043880458" or "546331545259212800"    in [role.id for role in ctx.message.author.roles]:
            await Breakouts.server_voice_state(member, mute=True, deafen=None)
    except Exception as e:
        await Breakouts.say("*I am being currently updated constantly, my apologies for my poor performance*")
@Breakouts.command(pass_context=True , aliases=['unmute'])
async def un_mute(ctx , member : discord.Member):
    try:
        if "553129176043880458" or "546331545259212800"    in [role.id for role in ctx.message.author.roles]:
            await Breakouts.server_voice_state(member, mute=False, deafen=None)
    except Exception as e:
        await Breakouts.say("*I am being currently updated constantly, my apologies for my poor performance*")
@Breakouts.command(pass_context=True , aliases=['deafen'])
async def no_sound(ctx , member : discord.Member):
    try:
        if "553129176043880458" or "546331545259212800"      in [role.id for role in ctx.message.author.roles]:
            await Breakouts.server_voice_state(member, mute=False, deafen=True)
    except Exception as e:
        await Breakouts.say("*I am being currently updated constantly, my apologies for my poor performance*")
@Breakouts.command(pass_context=True , aliases=['move'])
async def move_mem(ctx , member : discord.Member):
    channel = ctx.message.author.voice_channel
    try:
        if "553129176043880458" or "546331545259212800"    in [role.id for role in ctx.message.author.roles]:
            await Breakouts.move_member(member , channel)
            await Breakouts.say("*You have been moved for safety reasons*")
    except:
        await Breakouts.say("**USE THE MV COMMAND AND/OR SC TO SECURE CHANNELS\n,WARNING: THIS MAY BE A FALSE POSITIVE**")



@Breakouts.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    try:
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
         await Breakouts.say(embed=help_embed)
         await Breakouts.send_message(author , embed=help_embed)
    except:
        await Breakouts.say("**Cannot show help menu at the moment, please try again later**")


Breakouts.run(token)
