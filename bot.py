# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
#guild = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# @bot.event 
# async def on_message(message):
#     if message.author.bot:
#         return
#     if message.content.lower() == 'challenge':
#         await message.channel.send("")
#         #await message.channel


@bot.command(name='quote', help='Responds with a random quote from the archives')
async def nine_nine(ctx):
    quotes_list = [
        'Skate fast',
        'Bingo bango!',
        'Love is a mango',
    ]
    response = random.choice(quotes_list)
    await ctx.send(response)

@bot.command(name='mme', help='Mention test')
async def mention_me(ctx):
    await ctx.send(ctx.message.author.mention)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel', help='Creates a channel.')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        await ctx.send('Channel created')
    else:
        await ctx.send('Channel already exists!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



bot.run(token)
