import json

import discord
import sqlite3
import requests
from discord.ext import commands
from discord.ext import tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
bot.remove_command('help')

slash = SlashCommand(bot, sync_commands=True)

connection = sqlite3.connect('server.db')
async def on_ready():
    # задает статус бота
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f'/help'))
    print('BOT connected')


@bot.event
async def on_member_join(member):
    pass

bot.load_extension("cogs.audit_log")
bot.load_extension("cogs.voice_manager")
bot.load_extension("cogs.give_start_role")

bot.run('NzM0NzMzNjQ1OTAxNzI1NzY2.XxWABw.Gt57r8wuiNtprE4Ya-nsCnsjxHY')
