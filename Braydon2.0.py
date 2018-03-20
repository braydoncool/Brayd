import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import sys
import random

bot = commands.Bot(command_prefix = '^')
value = random.randint(1, 6)
age = random.randint(10, 67)
bot.remove_command('help')

@bot.event
async def on_ready():
    print ("Ready Now")
    print ("I am running on " + bot.user.name)
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx,user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find,", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name is jeff", color=0x00ff00)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Will Braydon")
    embed.add_field(name="Field", value="is it?", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Help Command", description="For Braydon2.0", color=0x010285)
    embed.set_footer(text="Braydon2.0 Help")
    embed.set_author(name="Help is here!!")
    embed.add_field(name=" Misc Commands", value="help,embed,info,dynopeople,baguette,davin", inline=True)
    embed.add_field(name=" Moderator Commands", value="kick,ban", inline=True)
    embed.add_field(name="Poll Commands", value="Coming Soon!", inline=True)
    embed.add_field(name="Modules", value="Coming Soon!", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def dynopeople(ctx):
    embed = discord.Embed(title="Khaaz", description="Chipped", color=0x010285)
    embed.set_footer(text="Coal")
    embed.set_author(name="Davin")
    embed.add_field(name="Ollie", value="NoobLance", inline=True)
    embed.add_field(name="GlitchMaster", value="MasterMeyers", inline=True)
    embed.add_field(name="Practiclycrp", value="Carti", inline=True)
    embed.set_footer(text="Dyno People")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def baguette(ctx):
    await bot.say("Hi Khaaz")

@bot.command(pass_context=True)
async def davin(ctx):
    await bot.say("{} have broken me".format(user.name))

@bot.command(pass_context=True)
async def roll(ctx):
    await bot.say(value)

@bot.command(pass_context=True)
async def guessmyage(ctx):
    await bot.say(age)

@bot.command(pass_context=True)
async def kick(ctx,user: discord.Member):
    kick(member)
    await bot.say("{} has been kicked from server".format(user.name))
    



                  


    
    

bot.run(process.env.BOT_TOKEN)
