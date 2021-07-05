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


def setup(client):
	client.add_cog(Moderation(client))
