import discord
import discord.ext 
import commands
from config import settings

bot = commands.Bo(command_prefix = settings['prefix'])
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')
bot.run(settings['token'])