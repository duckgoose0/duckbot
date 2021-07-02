import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event  # on bot startup
async def on_ready():
    print('duckbot is running...')


# bot info commands
@client.command()
async def bothelp(ctx):
    await ctx.send('''here\'s a list of commands you can currenly use:

//bot info
?bothelp > returns list of commands
?botping > returns bot latency

//simple response
?duck > quack
?goose > honk
?doggo > bork
?catto > mlem

//randomizers
?ask [query] > responds to a question with yes/maybe/no
?coin > flips a coin | aliases: ?flip and ?cointoss
?card > draws a random card from a standard deck of 52 | aliases: ?shuffle''')


@client.command()
async def botping(ctx):
    await ctx.send(f'The bot\'s latency is {round(client.latency * 1000)}ms.')


# simple response commands
@client.command()
async def duck(ctx):
    await ctx.send('quack')


@client.command()
async def goose(ctx):
    await ctx.send('honk')


@client.command()
async def doggo(ctx):
    await ctx.send('bork')


@client.command()
async def catto(ctx):
    await ctx.send('mlem')


# tools commands
@client.command()
async def ask(ctx, *, question):
    responses = ['Yes :grin:',
                 'Of course :grin:',
                 'Maybe :thinking:',
                 'I don\'t know :thinking:',
                 'No :pensive:',
                 'I don\'t think so :pensive:']
    await ctx.send(f'''> {question}
{random.choice(responses)}''')


@client.command(aliases=['flip', 'cointoss'])
async def coin(ctx):
    responses = ['heads', 'tails']
    await ctx.send(f'{random.choice(responses)}')


@client.command()
async def rand(ctx, min, max):  # not functioning yet
    await ctx.send(f'The number I have selected is **{random.randint(min, max)}')


@client.command(aliases=['shuffle'])
async def card(ctx):
    value = ['Ace',
             '2',
             '3',
             '4',
             '5',
             '6',
             '7',
             '8',
             '9',
             '10',
             'Jack',
             'Queen',
             'King']
    suit = ['Clubs',
            'Hearts',
            'Spades',
            'Diamonds']
    number = ['A',
              '2',
              '3',
              '4',
              '5',
              '6',
              '7',
              '8',
              '9',
              '10',
              'J',
              'Q',
              'K']
    symbol = [':clubs:',
              ':heart:',
              ':spades:',
              ':diamonds:']
    await ctx.send(f'I drew the {random.choice(value)} of {random.choice(suit)}.')


client.run(token)
