prefix = "."
token = ""
welcome_channel_id =
leave_channel_id =

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("My name is", bot.user.name)

@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(welcome_channel_id)
        try:
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name= "Welcome" ,value=f"**Hey,{member.mention}! Welcome in {member.guild.name}\nWe hope you will like our server!**", inline=False)
            embed.set_thumbnail(url=member.guild.icon_url)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(leave_channel_id)
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(name="Goodbye", value=f"**{member.mention} left the server.**", inline=False)
            embed.set_thumbnail(url=member.guild.icon_url)
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

bot.run(token)
