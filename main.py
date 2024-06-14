import os
import interactions
import asyncio
from interactions import Embed, File, slash_command, SlashContext, slash_option, OptionType
from lilb.coin_flip import CoinFlip
from lilb.helpers import Helpers

bot = interactions.Client()
helpers = Helpers()

@interactions.listen()
async def on_ready():
    print(f'Logged in as {bot.user}')

@slash_command(name='toss', description='Flip a coin')
async def toss(ctx: SlashContext):
    coin_side = CoinFlip()
    value = coin_side.flip()
    tossing_message = await ctx.send('Tossing coin 🪙', hidden=True)
    await asyncio.sleep(1)
    await tossing_message.edit(content=f'Got {value}')

@slash_command(name='toss_times')
@slash_option(name="times", description='Number of times to flip the coin',opt_type=OptionType.INTEGER,required=True)
async def toss_times(ctx: SlashContext, times: int):
    coin_side = CoinFlip()
    coin_side.flip_n_times(times)
    tossing_message = await ctx.send('Tossing coin', hidden=True)
    heads, tails = coin_side.get_results()
    await asyncio.sleep(1)
    await tossing_message.edit(f'Tossed {times} times, Got Heads: {heads} and Got Tails: {tails}')
    
'''
Return a random valorant map, includes all maps even those not in rotation
'''
@slash_command(name='map', description='Random Valorant map')
async def map(ctx: SlashContext):
    map_name,image_path = Helpers.get_random_map()
    
    # Send the map name and image
    with open(image_path, 'rb') as f:
        file = File(file=f, file_name=os.path.basename(image_path))
        embed = Embed(title=map_name)
        embed.set_image(url=f"attachment://{os.path.basename(image_path)}")
        await ctx.send(embeds=[embed], files=[file])

bot.load_extension("interactions.ext.jurigged")
bot.start(Helpers.get_env('DISCORD_TOKEN'))