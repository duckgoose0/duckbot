import discord
import os
from discord.ext import commands


class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['purge', 'delete'])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, num=6):
		try:
			await ctx.channel.purge(limit=num)
		except commands.MissingPermissions:
			await ctx.send('You don\'t have permission to use that command!')

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, *, reason=None):
			await member.kick(reason=reason)
			await ctx.send(f'{member} was kicked from the server.')

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to use that command!')
		elif isinstance(error, commands.BadArgument):
			await ctx.send('No user specified!')
		else: raise error


	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member, *, reason=None):
			await member.ban(reason=reason)
			await ctx.send(f'{member} was banned indefinitely from the server.')

	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send('You don\'t have permission to use that command!')
		elif isinstance(error, commands.BadArgument):
			await ctx.send('No user specified!')
		else: raise error


def setup(client):
	client.add_cog(Moderation(client))
