import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle

class CustomHelpCommand(commands.HelpCommand):
	def __init__(self):
		super().__init__()

	async def send_bot_help(self, mapping):
		helpMain = '''These are the things I can do right now! For more information on a specific command, just type `>>help [name of command]`.'''
		for cog in mapping:
			try:
				helpMain += (f'\n\n__**{cog.qualified_name}**__')
				for command in mapping[cog]:
					helpMain += (f'\n{command.qualified_name}')
			except AttributeError:
				pass
			
		helpMain += (f'\n\n**Help** <- you are here')
		await self.get_destination().send(helpMain)

	async def send_cog_help(self, cog):
		return await super().send_cog_help(cog)

	async def send_group_help(self, group):
		return await super().send_group_help(group)

	async def send_command_help(self, command):
		return await super().send_command_help(command)


client = commands.Bot(command_prefix='>>', help_command=CustomHelpCommand())
keep_alive()
token = os.environ['DISCORD_BOT_TOKEN']
status = cycle(['need help with the bot?', 'send >>help'])


@client.event  # bot birthday is july 1
async def on_ready():
	change_status.start()
	print('duckbot is running...')


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('The command you are trying to use does not exist.')
	else:
		raise error


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


@tasks.loop(seconds=5)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
