#import discord
import os
import interactions
from interactions import slash_command, SlashContext
#from discord.ext import commands
from lilb.coin_flip import CoinFlip

bot = interactions.Client()

@interactions.listen()
async def on_ready():
    print(f'Logged in as {bot.user}')

@slash_command(name='toss', description='Flip a coin')
async def toss(ctx: SlashContext):
    coin_side = CoinFlip()
    value = coin_side.flip()
    await ctx.send(f'Got {value}')



bot.start(os.getenv('DISCORD_TOKEN'))