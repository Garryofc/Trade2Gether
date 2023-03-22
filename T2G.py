import sys 
sys.dont_write_bytecode = True
import discord
from discord import client
from discord.ext import commands
import asyncio
import logging
from discord import app_commands
from colorama import Fore
import colorama
import assets.promotion.promotion_levels as config2
import assets.config as config
from pycoingecko import CoinGeckoAPI
import json
import pandas as pd
from datetime import datetime
import requests
import openai
import matplotlib.pyplot as plt
colorama.init()

response = requests.get("https://newsapi.org/v2/everything?q=crypto&apiKey=53cfa62aacb3433e89fdfbc25c7daf7a")
data = json.loads(response.text)
openai.api_key = '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'
all_articles = data['articles']


client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
client = commands.Bot(command_prefix='/', intents=discord.Intents.all(), application_id="1084530469284106240")
# Logging info
logging.basicConfig(filename="assets/logs/log.txt", level=logging.INFO, format="%(asctime)s %(message)s")

@client.event
async def on_ready():
    activity=discord.Activity(type=discord.ActivityType.streaming, name="/help")
    await client.change_presence(status=discord.Status.idle ,activity=activity)
    print("""
$$$$$$$$\  $$$$$$\   $$$$$$\  
\__$$  __|$$  __$$\ $$  __$$\ 
   $$ |   \__/  $$ |$$ /  \__|
   $$ |    $$$$$$  |$$ |$$$$\ 
   $$ |   $$  ____/ $$ |\_$$ |
   $$ |   $$ |      $$ |  $$ |
   $$ |   $$$$$$$$\ \$$$$$$  |
   \__|   \________| \______/ 
    """)
    synced = await client.tree.sync()
    print("Slash CMDs Synced " + str(len(synced)) + " Commands")


@client.tree.command(name='dailynews', description='Prints news')
async def news(interaction: discord.Interaction):
    if config.NEWS == True:
        if interaction.user.guild_permissions.administrator:
            channel = client.get_channel(1087405120788115528)
            try:
                count = 0
                for each in all_articles:
                    count += 1
                    await channel.send(f"**{count}:- {each['title']}**\n*{each['content']}*\n{each['url']}")
                    if count == 5:
                        break
            except Exception as e:
                print(e) 
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                    color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


class MyView(discord.ui.View):
    @discord.ui.button(label="Produkt",row=0, style=discord.ButtonStyle.primary) 
    async def button_callback(self, interaction, button):
        await interaction.response.send_message("1")
    @discord.ui.button(label="Produkt2",row=0, style=discord.ButtonStyle.primary)
    async def second_callback(self, interaction, button):
        await interaction.response.send_message("1")
    @discord.ui.button(label="Produkt3",row=0, style=discord.ButtonStyle.primary)
    async def third_callback(self, interaction, button):
        await interaction.response.send_message("1")
    @discord.ui.button(label="Produkt4",row=1, style=discord.ButtonStyle.primary) 
    async def fourth_callback(self, interaction, button):
        await interaction.response.send_message("1")
    @discord.ui.button(label="Produkt5",row=1, style=discord.ButtonStyle.primary)
    async def five_callback(self, interaction, button):
        await interaction.response.send_message("1")
    @discord.ui.button(label="Produkt6",row=1, style=discord.ButtonStyle.primary)
    async def six_callback(self, interaction, button):
        await interaction.response.send_message("1")



# <------Joining Member------->
@client.event
async def on_member_join(member: discord.Member):
    try:
        print("Recognised that a member called " + member.name + " joined the Server")
        if member.name == 'filip' or member.name == 'jnvck.crypto':
            if member.discriminator == '0007' or member.discriminator == '4471':
                member.ban()
            else:
                channel = client.get_channel(1083483864728608858)
                server = member.guild
                embed = discord.Embed(title=f"**Welcome {member.name}**👋" ,
                                    color=discord.Color.blue())
                embed.add_field(name="📚**Rules**",value="Please make sure that you read the rules")
                embed.add_field(name="❓**Support**",value="If you have any questions open a ticket ")
                embed.add_field(name="🍿**Enjoy**",value=f"Have Fun and enjoy chatting and talking on the Server **{server.name}**")
                embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
                await channel.send(embed=embed)
        else:
            channel = client.get_channel(1083483864728608858)
            server = member.guild
            embed = discord.Embed(title=f"**Welcome {member.name}**👋" ,
                                color=discord.Color.blue())
            embed.add_field(name="📚**Rules**",value="Please make sure that you read the rules")
            embed.add_field(name="❓**Support**",value="If you have any questions open a ticket ")
            embed.add_field(name="🍿**Enjoy**",value=f"Have Fun and enjoy chatting and talking on the Server **{server.name}**")
            embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
            await channel.send(embed=embed)
    except Exception as e:
        print(e) 




# <---------ban command---------->
@client.tree.command(name="ban", description="ban a user")
async def ban_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if config.BAN == True:
        if interaction.user.guild_permissions.ban_members:
            await user.ban(reason=reason)
            embed = discord.Embed(title=f"**{user.name} was banned by {interaction.user.name}**",
                                color=discord.Colour.random())
            embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%Y-%m-%d"))
            embed.add_field(name="🆔**User ID**", value=user.id)
            embed.add_field(name="💬**Reason**", value=reason)
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
            logging.info(f"Command = ban ; Author = {interaction.user.name} ; Banned = {str(user.name)}; Reason = {reason}")
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**", color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)





# <------kick command----->
@client.tree.command(name="kick", description="kick a user")
async def kick(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if config.KICK == True:
        channel = interaction.channel
        server = interaction.guild
        if interaction.user.guild_permissions.kick_members:
            await user.kick(reason=reason)
            embed = discord.Embed(title=f"**{user.name} was kicked by {interaction.user.name}**",
                                color=discord.Colour.random())
            embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%Y-%m-%d"))
            embed.add_field(name="🆔**User ID**", value=user.id)
            embed.add_field(name="💬**Reason**", value=reason)
            embed.set_thumbnail(url=server.icon.url)
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            logging.info(f"Command = kick ; Author = {interaction.user.name} ; kicked = {str(user.name)}; Reason = {reason}")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)

    



@client.tree.command(name="gen", description="generates an AI message")
async def gen(interaction: discord.Interaction, text: str):
    if config.GENERATOR == True:
        await interaction.response.defer()
        response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"{text}\n",
                    max_tokens=350,
                    temperature=1,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                ).choices[0].text
        print(f'{Fore.BLUE}Author: {interaction.user.name}')
        print(f'{Fore.CYAN}Message: {text}')
        print(f'{Fore.GREEN}Response: {response}{Fore.RESET}')
        embed = discord.Embed(title=f"**AI to {interaction.user.name}**",
                                color=discord.Colour.random())
        embed.add_field(name='**User -->**', value=text)
        embed.add_field(name="🔍**AI -->**", value= response)
        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
        await asyncio.sleep(5)
        await interaction.followup.send(embed=embed)
        logging.info(f"Command = gen ; Author = {interaction.user.name} ; Message = {text}; Response = {response}")
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)





# <------help command---------->
@client.tree.command(name="help", description="help command")
async def help(interaction: discord.Interaction):
    if config.HELP_COMMAND == True:
        embed = discord.Embed(title="**Command-List for Garry/HyperAI-Bot**", color=discord.Colour.random())
        embed.add_field(name="🌐**help**", value="list of all commands")
        embed.add_field(name="🎭**avatar**", value="shows a users avatar")
        embed.add_field(name="ℹ️**serverinfo**", value="gives info about the server")
        embed.add_field(name="⚙️**admin**", value="list all admin commands")
        embed.add_field(name="ℹ️**userinfo**", value="gives information about an user")
        embed.add_field(name="🔰**roles**", value="list all server roles")
        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="owner", description = "shows name of an owner")
async def owner(interaction: discord.Interaction):
    embed = discord.Embed(title="**Owner** -->", description= "Owner of this discord bot is Garry#5555, and his contributor HyperAI co.", color=discord.Colour.random())
    await interaction.response.send_message(embed=embed)



# <---------serverinfo command---------->
@client.tree.command(name="serverinfo", description="shows you basic info about the server")
async def serverinfo(interaction: discord.Interaction):
    if config.SERVER_INFO == True:
        server = interaction.guild
        embed = discord.Embed(title=f"Server Info for {server.name}", color=discord.Colour.random())
        embed.add_field(name="💬**Server Name**", value=server.name)
        embed.add_field(name="🆔**Server ID**", value=server.id)
        embed.add_field(name="📆**Created On**", value=server.created_at.strftime('%Y-%m-%d'))
        embed.add_field(name="👑**Server Owner**", value=server.owner)
        embed.add_field(name="👥**Server Member Count**", value=server.member_count)
        embed.set_thumbnail(url=server.icon.url)
        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else: 
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)



@client.tree.command(name="admin", description="lists you all admin commands")
async def admin(interaction: discord.Interaction):
    if config.ADMIN == True:
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="**Admin-Command List**", color=discord.Colour.random())
            embed.add_field(name="🌐**.kick**", value="kicks a user")
            embed.add_field(name="🚫**.ban**", value="bans a user")
            embed.add_field(name="🧼**.clear**", value="clear chat messages")
            embed.add_field(name="🔐**.mute**", value="chat-locks a user")
            embed.add_field(name="🔓**.unmute**", value="unlock a user (from the chat)")
            embed.add_field(name="⚙️**.admin**", value="list all admin commands")
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)



@client.tree.command(name='rules', description='Here are some general rules you may want to consider for your Discord server')
async def rules(interaction: discord.Interaction):
    if config.RULES == True:
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="**Rules**", color=discord.Colour.blurple())
            embed.add_field(name="**1**", value="Be respectful to all members. Harassment, hate speech, and discriminatory language will not be tolerated.")
            embed.add_field(name="**2**", value="No spamming or excessive self-promotion. You can share your content or streams, but please do so within reason and in appropriate channels.")
            embed.add_field(name="**3**", value="Keep conversations in the appropriate channels. Avoid derailing discussions or posting irrelevant content.")
            embed.add_field(name="**4**", value="No NSFW content. This includes text, images, and links.")
            embed.add_field(name="**5**", value="No sharing of personal information. Do not share personal information or sensitive data of others.")
            embed.add_field(name="**6**", value="Follow Discord's Terms of Service and Community Guidelines.")
            embed.add_field(name="**7**", value="Any violations of the rules will result in disciplinary action, ranging from warnings to permanent bans.")
            embed.add_field(name="**8**" ,value="Remember, rules are meant to create a safe and enjoyable environment for all members. It's important to have clear guidelines in place to ensure that everyone can feel comfortable participating in discussions and sharing their ideas.")
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                    color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)



@client.tree.command(name='shop', description='shows products to sale')
async def shop(interaction: discord.Interaction):
    if config.SHOP == True:
        embed = discord.Embed(title="**Shop**", description= 'All information listed in the disclaimer section applies to the products (risk, disclaimer 1 and 2/2)',color=discord.Colour.blurple())
        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
        await interaction.response.defer()
        await asyncio.sleep(1)
        await interaction.followup.send(embed=embed, view=MyView())
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='disclaimer', description='disclaimer')
async def disclaimer(interaction: discord.Interaction):
    if config.DISCLAIMER == True:
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="**Dislaimer**", color=discord.Colour.blurple())
            embed.add_field(name="**Disclaimer 1/2**", value="""
All information published here by the creators or other users should not be taken as financial or investment advice. The messages posted on this server do not encourage the purchase of cryptocurrencies, they are only opinions that the members of the server can view for free if they wish. All content is for educational or entertainment purposes only. You should not use the information posted on this server to make investment or financial decisions. Always do your own research (from multiple sources) and opinion first. Any decision based on the information contained herein is made by Discord members at their own risk and any loss suffered by the users of the server is solely their own responsibility. Trade2Gether does not guarantee any results. Trading is very complex and a process where most people lose money. Previous success does not guarantee future success.
            """)
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                    color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)





@client.tree.command(name='accept', description='accept embed')
async def accept(interaction: discord.Interaction):
    if config.ACCEPT == True:
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="**Confirmation**", description='Add :white_check_mark: reaction if you accept',color=discord.Colour.blurple())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                        color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='info', description="Send's you a basic info about **T2G**")
async def info(interaction: discord.Interaction):
    if config.INFO == True:
        try:
            f = open('assets/info/info.txt', 'r')
            f2 = open('assets/info/info2.txt', 'r')
            f3 = open('assets/info/info3.txt', 'r')
            info = f.read()
            info2 = f2.read()
            info3 = f3.read()
            embed = discord.Embed(title='**Information**', color=discord.Colour.random())
            embed.add_field(name='1', value= info)
            embed.add_field(name='2', value= info2)
            embed.add_field(name='3', value= info3)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e) 
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)



@client.tree.command(name='disclaimer2', description='disclaimer2')
async def disclaimer2(interaction: discord.Interaction):
    if config.DISCLAIMER == True:
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="**Disclaimer**", color=discord.Colour.blurple())
            embed.add_field(name="**Disclaimer 2/2**", value="""
By purchasing a membership, you agree that if you no longer wish to renew your subscription. You are responsible for canceling your membership on the upgrade.chat page in the subscription section. If you do not do so the day before your membership renewal and the money is deducted, you lose the right to a refund.
            """)
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                    color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='risk', description='risk')
async def risk(interaction: discord.Interaction):
    if config.RISK == True:
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="**Risk**", color=discord.Colour.blurple())
            embed.add_field(name="**Risk Notice**", value="""
Risk Warning: CFDs and Cryptocurrency Investments are complex instruments and if you trade them there is a risk that you will lose money quickly due to financial leverage. 
82% of retail investors' accounts end up losing money when trading with this provider. 
Think about whether you understand how CFDs and cryptocurrencies work and whether you can afford to take such a risk with your money.
            """)
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                    color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='fun', description='shows a definition of fun')
async def fun(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title='**FUN**', description='''
░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░
░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░
░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░
░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░
░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░
██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░
█░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░
█░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░
█░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░
█░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄
█░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██
█░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██
▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀
░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░
░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░
░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░
░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░
░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░
░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░
░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
''', color= discord.Colour.random())
        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed, ephemeral=True)


# <----------basic clear command---------->
@client.tree.command(name="clear", description="clears chat messages")
async def clear(interaction: discord.Interaction, amount: int = 0):
    if config.CLEAR == True:
        channel = interaction.channel
        if interaction.user.guild_permissions.manage_messages:
            try:
                await interaction.response.defer()
                await channel.purge(limit=amount + 1)
                embed = discord.Embed(title=f"{interaction.user.name} cleared {amount} Messages",
                                    color=discord.Colour.random())
                embed.add_field(name="🆔 **User ID**", value=interaction.user.id)
                embed.add_field(name="📆**Cleared Messages At**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await asyncio.sleep(2)
                await interaction.followup.send(embed=embed)
                logging.info(f"Command = clear ; Author = {interaction.user.name} ; Cleared = {amount}")
            except ValueError:
                embed = discord.Embed(title="**Please enter a valid number of messages to delete.**",
                                    color=discord.Colour.random())
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else: 
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)



# <-------unmute-command---------->
@client.tree.command(name="unmute", description="unmutes a user from the chat")
async def unmute_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if config.MUTE == True:
        channel = interaction.channel
        if interaction.user.guild_permissions.manage_messages:
            await channel.set_permissions(user, send_messages=True)
            embed = discord.Embed(
                title=f"**{user.name} has been unmuted by {interaction.user.name}**",
                color=discord.Colour.random())
            embed.add_field(name="🆔**User ID**", value=user.id)
            embed.add_field(name="💬**Reason**", value=reason)
            embed.add_field(name="📆**Unmuted on**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)

# <-------mute-command------->
@client.tree.command(name="mute", description="mutes a user from the chat")
async def mute_user(interaction: discord.Interaction, user: discord.User, reason: str = None, time: int = 0):
    if config.MUTE == True:
        channel = interaction.channel
        if interaction.user.guild_permissions.manage_messages:
            await channel.set_permissions(user, send_messages=False)
            embed = discord.Embed(
                title=f"**{user.name} has been muted by {interaction.user.name}**",
                color=discord.Colour.red())
            embed.add_field(name="🆔**User ID**", value=user.id)
            embed.add_field(name="💬**Reason**", value=reason)
            embed.add_field(name="📆**Muted on**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name="🕒**Muted for**", value=f"{time} seconds")
            embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
            await interaction.response.defer()
            await interaction.followup.send(embed=embed)
            await asyncio.sleep(time)
            await channel.set_permissions(user, send_messages=True)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)

#<------info command------>

@client.tree.command(name='broadcast', description='Broadcasts message to announcement room')
async def broadcast(interaction: discord.Interaction, message: str):
    if config.BROADCAST == True:
        if interaction.user.guild_permissions.administrator:
            channel = client.get_channel(1083483909351800914)
            embed = discord.Embed(title='** :gem: Announcement :gem: ** ', color=discord.Color.blurple())
            embed.add_field(name=message, value=f'For the Trade2Gether team: {interaction.user.name}')
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await channel.send(embed=embed)
            embed2 = discord.Embed(title='**Sended** ', color=discord.Color.blurple())
            await interaction.response.send_message(embed=embed2)
        else:
            embed = discord.Embed(title="**You don't have the permission for that Command**",
                                color=discord.Colour.random())
            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else: 
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


# for getting userinfo

@client.tree.command(name="userinfo", description="gives information about a user")
async def userinfo(interaction: discord.Interaction, user: discord.User):
    if config.USER_INFO == True:
        rolelist = []
        for role in user.roles:
            if role.name != "@everyone":
                rolelist.append(role.mention)
        b = ",".join(rolelist)

        embed = discord.Embed(title=f"**User Info about {user}**",
                            color=discord.Colour.purple())
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="📆**Created at**",value=user.created_at.strftime("%Y-%m-%d"))
        embed.add_field(name="🕗**Joined at**", value=user.joined_at.strftime("%Y-%m-%d"))
        embed.add_field(name=f"🔰**Role:** ({len(rolelist)})",value="".join([b]))
        embed.add_field(name=f"🎖**Top-Role**",value=user.top_role.mention)
        embed.add_field(name=f"🏆**Booster**",value=f'{"Yes" if user.premium_since else "No"}')
        embed.add_field(name="🤖**Bot**",value=f"{'Yes' if user.bot else 'No'}")
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else: 
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='brokers', description='shows a brokers we recommend')
async def brokers(interaction: discord.Interaction):
    if config.BROKERS == True:
        embed = discord.Embed(title='**Brokers**',color=discord.Colour.yellow())
        embed.add_field(name='**1**', value='[Binance](https://accounts.binance.com/en/register?ref=523861052&gclid=Cj0KCQjwtsCgBhDEARIsAE7RYh2-pfYxCnRIeruJAq6HSleAxj9jUZXlDt1fvBnclj-S-XtmgI0vg94aAk-gEALw_wcB)')
        embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


#<-------Avatar-Command------------>
# shows a discord users avatar  as "big" format in the chat
@client.tree.command(name="avatar", description="prints the users avatar")
async def avatar(interaction: discord.Interaction, user: discord.User):
    if config.AVATAR == True:
        userAvatarUrl = user.avatar.url
        embed = discord.Embed(title=f"**{user}s Avatar:**",color=discord.Colour.yellow()).set_image(url=user.avatar.url)
        embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='partners', description='shows our partners')
async def partners(interaction: discord.Interaction):
    if config.PARTNER == True:
        embed = discord.Embed(title=f"**Our Partners:**",color=discord.Colour.random())
        embed.add_field(name='**1**', value='[WolfMedia](https://wolf-media.cz)')
        embed.add_field(name='**2**', value='[FANCYGANCY](https://fancygancy.com/)')
        embed.add_field(name='**3**', value='[HyperAI](https://discord.gg/bahaf5XPRs)')
        embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name='chad', description='Sends a chad gif')
async def chad(interaction: discord.Interaction, user: discord.User):
    if config.CHAD == True:
        embed = discord.Embed(title=f"**{user.name} is truly a chad**",color=discord.Colour.random())
        embed.set_image(url="https://media.tenor.com/epNMHGvRyHcAAAAd/gigachad-chad.gif")
        embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name='skull', description='Sends a skull gif')
async def skull(interaction: discord.Interaction):
    if config.SKULL == True:
        embed = discord.Embed(title=f"**Skull**",color=discord.Colour.random())
        embed.set_image(url="https://media.tenor.com/g1bZgt4-tL4AAAAC/skull.gif")
        embed.set_footer(text="⭐  • Garry/HyperAI | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title='Error', description = 'Command is deactivated', color=discord.Colour.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name='signal', description='sends signal')
async def signal(interaction: discord.Interaction, chart: str, sl: str, tp: str, tp2: str, tp3: str, ep: str):
    try:
        if config.SIGNAL == True:
            if interaction.user.guild_permissions.administrator:
                embed = discord.Embed(title='Signal', color=discord.Colour.random())
                embed.add_field(name='Chart:', value=chart, inline= False)
                embed.add_field(name='SL:', value=sl, inline= False)
                embed.add_field(name='TP1:', value=tp, inline= False)
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                if tp2 == None:
                    embed.add_field(name='EP:', value=ep, inline= False)
                    embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                    await interaction.response.send_message(embed=embed)
                else:
                    if tp3 == None:
                        embed.add_field(name='TP2:', value=tp2, inline= False)
                        embed.add_field(name='EP:', value=ep, inline= False)
                        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                        await interaction.response.send_message(embed=embed)
                    else:
                        embed.add_field(name='TP2:', value=tp2, inline= False)
                        embed.add_field(name='TP3:', value=tp3, inline= False)
                        embed.add_field(name='EP:', value=ep, inline= False)
                        embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                        await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(title="**You don't have the permission for that command**", color=discord.Colour.random())
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title='Error', description='Command is deactivated', color=discord.Colour.red())
            await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(e) 


@client.tree.command(name='beginners', description='Sends a beginner message')
async def beginner(interaction: discord.Interaction):
    try:
        if config.BEGINNER == True:
            if interaction.user.guild_permissions.administrator:
                embed = discord.Embed(title='Beginners', color=discord.Colour.random())
                embed.add_field(name='TP', value='Take Profit', inline= False)
                embed.add_field(name='SL', value='Stop Loss', inline= False)
                embed.add_field(name='EP', value='Entry Point', inline= False)
                embed.add_field(name='Long', value='Buy', inline= False)
                embed.add_field(name='Short', value='Sell', inline= False)
                embed.add_field(name='LM', value='Limit Order', inline= False)
                embed.add_field(name='RRR', value='Risk/Reward Ratio', inline= False)
                embed.add_field(name='MM', value='Money Management', inline= False)
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(title="**You don't have the permission for that command**", color=discord.Colour.random())
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title='Error', description='Command is deactivated', color=discord.Colour.red())
            await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(e) 






@client.tree.command(name='promote', description='Gives a Special **Permision**')
async def star(interaction: discord.Interaction, user: discord.Member, reason: str):
    try:
        if config.STAR:
            if interaction.user.guild_permissions.administrator:
                if config2.PROMOTION is None:
                    embed = discord.Embed(title='Error', description='Set promotion level', color=discord.Colour.red())
                    await interaction.response.send_message(embed=embed)
                else:
                    if config2.PROMOTION == 3:                        
                        role_id = 1086268195549220904
                        role = interaction.guild.get_role(role_id)
                        if role in user.roles:
                            embed = discord.Embed(title='Error', description='User is already promoted', color=discord.Colour.red())
                            await interaction.response.send_message(embed=embed)
                        else:    
                            await user.add_roles(role)
                            embed = discord.Embed(title='**Promotion**', color=discord.Colour.random())
                            embed.add_field(name=f'**{interaction.user.name} promoted {user.name} for {reason}**', value='')
                            
                            if user.avatar:
                                embed.set_image(url=user.avatar.url)
                                
                            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                            await interaction.response.send_message(embed=embed)
                    elif config2.PROMOTION == 2:
                        role_id = 1083488873407062067
                        role = interaction.guild.get_role(role_id)
                        if role in user.roles:
                            embed = discord.Embed(title='Error', description='User is already promoted', color=discord.Colour.red())
                            await interaction.response.send_message(embed=embed)
                        else:    
                            await user.add_roles(role)
                            embed = discord.Embed(title='**Promotion**', color=discord.Colour.random())
                            embed.add_field(name=f'**{interaction.user.name} promoted {user.name} for {reason}**', value='')
                            
                            if user.avatar:
                                embed.set_image(url=user.avatar.url)
                                
                            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                            await interaction.response.send_message(embed=embed)
                    elif config2.PROMOTION == 1:
                        role_id = 1083511219169787934
                        role = interaction.guild.get_role(role_id)
                        if role in user.roles:
                            embed = discord.Embed(title='Error', description='User is already promoted', color=discord.Colour.red())
                            await interaction.response.send_message(embed=embed)
                        else:    
                            await user.add_roles(role)
                            embed = discord.Embed(title='**Promotion**', color=discord.Colour.random())
                            embed.add_field(name=f'**{interaction.user.name} promoted {user.name} for {reason}**', value='')
                            
                            if user.avatar:
                                embed.set_image(url=user.avatar.url)
                                
                            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                            await interaction.response.send_message(embed=embed)
                    else:
                        embed = discord.Embed(title='Error', description='Promotion level not valid', color=discord.Colour.red())
                        await interaction.response.send_message(embed=embed)             
            else:
                embed = discord.Embed(title="**You don't have the permission for that command**", color=discord.Colour.random())
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title='Error', description='Command is deactivated', color=discord.Colour.red())
            await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(e) 
    
@client.tree.command(name= 'demote', description='Removes a Special **Permision**')
async def star(interaction: discord.Interaction, user: discord.Member):
    try:
        if config.STAR:
            if interaction.user.guild_permissions.administrator:
                if config2.PROMOTION is None:
                    embed = discord.Embed(title='Error', description='Set promotion level', color=discord.Colour.red())
                    await interaction.response.send_message(embed=embed)
                else: 
                    if config2.PROMOTION == 3:
                        role_id = 1086268195549220904
                        role = interaction.guild.get_role(role_id)
                        if role in user.roles:
                            await user.remove_roles(role)
                            embed = discord.Embed(title='**Demotion**', color=discord.Colour.random())
                            embed.add_field(name=f'**{interaction.user.name} demoted {user.name}**', value='')
                            await interaction.response.send_message(embed=embed)
                        else:    
                            embed = discord.Embed(title='Error', description='User is already demoted', color=discord.Colour.red())
                            await interaction.response.send_message(embed=embed)
                            if user.avatar:
                                embed.set_image(url=user.avatar.url)
                                
                            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                            await interaction.response.send_message(embed=embed)
                    elif config2.PROMOTION == 2:
                        role_id = 1083488873407062067
                        role = interaction.guild.get_role(role_id)
                        if role in user.roles:
                            await user.remove_roles(role)
                            embed = discord.Embed(title='**Demotion**', color=discord.Colour.random())
                            embed.add_field(name=f'**{interaction.user.name} demoted {user.name}**', value='')
                            await interaction.response.send_message(embed=embed)
                        else:    
                            embed = discord.Embed(title='Error', description='User is already demoted', color=discord.Colour.red())
                            await interaction.response.send_message(embed=embed)
                            if user.avatar:
                                embed.set_image(url=user.avatar.url)
                                
                            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                            await interaction.response.send_message(embed=embed)
                    elif config2.PROMOTION == 1:
                        role_id = 1083511219169787934
                        role = interaction.guild.get_role(role_id)
                        if role in user.roles:
                            await user.remove_roles(role)
                            embed = discord.Embed(title='**Demotion**', color=discord.Colour.random())
                            embed.add_field(name=f'**{interaction.user.name} demoted {user.name}**', value='')
                            await interaction.response.send_message(embed=embed)
                        else:    
                            embed = discord.Embed(title='Error', description='User is already demoted', color=discord.Colour.red())
                            await interaction.response.send_message(embed=embed)
                            if user.avatar:
                                embed.set_image(url=user.avatar.url)
                                
                            embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                            await interaction.response.send_message(embed=embed)
                    else:
                        embed = discord.Embed(title='Error', description='Promotion level not valid', color=discord.Colour.red())
                        await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(title="**You don't have the permission for that command**", color=discord.Colour.random())
                embed.set_footer(text="⭐ • Garry/HyperAI | Systems")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title='Error', description='Command is deactivated', color=discord.Colour.red())
            await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(e) 

client.run(config.TOKEN)