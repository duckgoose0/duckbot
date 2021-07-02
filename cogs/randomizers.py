import discord
import os
import random
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, commands):
        self.commands = commands

    @commands.command()
    async def ask(ctx, *, question):
        responses = ['Yes :grin:',
                     'Of course :grin:',
                     'Maybe :thinking:',
                     'I don\'t know :thinking:',
                     'No :pensive:',
                     'I don\'t think so :pensive:']
        await ctx.send(f'''> {question}
{random.choice(responses)}''')

    @commands.command(aliases=['flip', 'cointoss'])
    async def coin(ctx):
        responses = ['heads', 'tails']
        await ctx.send(f'{random.choice(responses)}')


# @commands.command()
# async def rand(ctx, min, max):  # not functioning yet
#    await ctx.send(f'The number I have selected is {random.randint(min, max)}')

    @commands.command(aliases=['shuffle'])
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


def setup(client):
    client.add_Cog(Info(client))
