import discord
import os
from discord.ext import commands
from lilb.coin_flip import CoinFlip



bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
@bot.command()
async def toss(ctx):
    coin_side = CoinFlip()
    value = coin_side.flip()
    await ctx.send(f'Got {value}')

@bot.command()
async def help(ctx):
    help_command = """
    .toss - Toss a coin and returns the result
    .help - Display this help message
"""
    await ctx.send(help_command)


bot.run(os.getenv('DISCORD_TOKEN'))