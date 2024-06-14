import os
import interactions
import asyncio
from interactions import Embed, File, slash_command, SlashContext, slash_option, OptionType, SlashCommandChoice
from lilb.coin_flip import CoinFlip
from lilb.helpers import Helpers
from lilb.quotes import Quotes

bot = interactions.Client()
quotes_key = Helpers.read_multi_line_file('config/quotes_keyword.txt')



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

@slash_command(name='toss_times', description='Flip a coin multiple times')
@slash_option(name="times", description='Number of times to flip the coin',opt_type=OptionType.INTEGER,required=True)
async def toss_times(ctx: SlashContext, times: int):
    coin_side = CoinFlip()
    coin_side.flip_n_times(times)
    tossing_message = await ctx.send('Tossing coin 🪙', hidden=True)
    heads, tails = coin_side.get_results()
    await asyncio.sleep(1)
    await tossing_message.edit(content=f'Tossed {times} times, Got Heads: {heads} and Got Tails: {tails}')
    
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

@slash_command(name='quote', description='Knowlege from the wise')
@slash_option(name="type", description='Type of quote',opt_type=OptionType.STRING,required=True,choices=[
    SlashCommandChoice(name='inspirational', value='inspirational'),
    SlashCommandChoice(name='love', value='love'),
    SlashCommandChoice(name='life', value='life'),
    SlashCommandChoice(name='motivational', value='motivational'),
    SlashCommandChoice(name='pain', value='pain'),
    SlashCommandChoice(name='random', value='random')
])
async def get_quotes(ctx: SlashContext, type: str):
    quotes = Quotes()
    value = quotes.get_quote(type)
    quote_message = await ctx.send(f'Getting your desired quote of {type} from my wikipedia', hidden=True)
    await asyncio.sleep(1)
    await quote_message.edit(content=f"** Ah here you go: {value} **")
    
bot.load_extension("interactions.ext.jurigged")
bot.start(Helpers.get_env('DISCORD_TOKEN'))