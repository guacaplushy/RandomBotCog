import os
from serv import serveron, app
from dotenv import load_dotenv
import discord
import random
from discord.ext import commands

@app.route("/users")
def users():
  info = f'{len(bot.users)} users {len(bot.guilds)} servers'
  return str(info)

load_dotenv()
bot_token = os.getenv('auth_token')

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('rb.', 'Rb.', 'RB.', 'rB.'), description='A bot for random value and random value related things.', case_insensitive=True, intents = discord.Intents.all())

class Help(commands.MinimalHelpCommand):
    async def send_pages(self):
        hexlist = '01234567890abcdef'
        colorhex = ''
        for makecolor in range(0,6):
          genhex = random.choice(hexlist)
          colorhex = colorhex + genhex
        color = discord.Color(int(colorhex, 16))
        destination = self.get_destination()
        e = discord.Embed(description='', color=color)
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = Help(no_category = 'Help')

bot.load_extension('cogs.Choosers')
bot.load_extension('cogs.Events')
bot.load_extension('cogs.Generators')
bot.load_extension('cogs.Shufflers')
bot.load_extension('cogs.Values')
bot.load_extension('cogs.DevOnly')

serveron()

bot.run(bot_token)