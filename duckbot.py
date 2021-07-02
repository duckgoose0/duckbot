import discord
import os
from discord.ext import commands


client = commands.Bot(command_prefix='?')
token = 'ODYwMjQwMDY5MzE3ODg2MDA0.YN4W_w.ik_xssMGk81Q_uSY9gcz-GJYBnw'


@client.command()
async def bothelp(ctx):
    await ctx.send('''here\'s a list of commands you can currenly use:

//bot info
?bothelp > returns list of commands
?botping > returns bot latency

//server tools
?clear [int] > deletes [int] number of messages in channel. if [int] is not specified, default is 5 | aliases: ?purge, ?delete

//simple response
?duck > quack
?goose > honk
?doggo > bork
?catto > mlem

//randomizers
?ask [query] > responds to a question with yes/maybe/no
?coin > flips a coin | aliases: ?flip, ?cointoss
?card > draws a random card from a standard deck of 52 | aliases: ?shuffle''')


@client.command()
async def botping(ctx):
    await ctx.send(f'The bot\'s latency is {round(client.latency * 1000)}ms.')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
