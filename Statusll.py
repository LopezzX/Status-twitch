import discord
from discord.ext import commands
import datetime
from pystyle import Colors, Colorate

bot = commands.Bot(command_prefix = '!')

print(Colorate.Horizontal(Colors.rainbow,"""    


██╗      ██████╗ ██████╗ ███████╗███████╗███████╗
██║     ██╔═══██╗██╔══██╗██╔════╝╚══███╔╝╚══███╔╝
██║     ██║   ██║██████╔╝█████╗    ███╔╝   ███╔╝ 
██║     ██║   ██║██╔═══╝ ██╔══╝   ███╔╝   ███╔╝  
███████╗╚██████╔╝██║     ███████╗███████╗███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝

"""))
token = input("Enter Token : ")
status = input("Enter Status : ")

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name= status,
        url = "https://twitch.tv/twitch"
    )
    print('Streaming [-] ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)