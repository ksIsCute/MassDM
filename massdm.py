import discord
from discord.ext import commands
import sys, time
class colors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  RESET = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

print(colors.OKCYAN + """
          ╔═╗╔═╦═══╦═══╦═══╗╔═══╦═╗╔═╗
          ║║╚╝║║╔═╗║╔═╗║╔═╗║╚╗╔╗║║╚╝║║
          ║╔╗╔╗║║─║║╚══╣╚══╗─║║║║╔╗╔╗║
          ║║║║║║╚═╝╠══╗╠══╗║─║║║║║║║║║
          ║║║║║║╔═╗║╚═╝║╚═╝║╔╝╚╝║║║║║║
          ╚╝╚╝╚╩╝─╚╩═══╩═══╝╚═══╩╝╚╝╚╝
------------+ Created By Ks#1000 +-----------
""")
bot = commands.Bot(command_prefix = ":")
def printslow(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
token = input(colors.OKGREEN + "What is your token?" + colors.RESET + "\n")
messagea = input(colors.OKGREEN + "What is your message?" + colors.RESET + "\n")
@bot.event
async def on_connect():
  friends = []
  for i in bot.user.friends:
    friends.append(i)
  print(colors.HEADER + "Starting...")
  printslow(f"Sending message to {len(friends)} friends..")
  for i in friends:
    try:
      await i.send(messagea)
      print(colors.OKBLUE + f"Message sent to: {i.name}")
    except Exception as err:
      print(f"Error sending DM to {i.name}: {err}")
  print(colors.RESET + "Done sending messages!")

bot.run(token, bot=False)
