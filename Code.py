import discord
import multiprocessing
from discord.ext import commands

prefix = "."



def read_tokens_from_file(file_path):
    with open(file_path, "r") as file:
        tokens = [line.strip() for line in file if line.strip()]
    return tokens


async def main():
    token_file = "tokens.txt"
    bot_tokens = read_tokens_from_file(token_file)




async def raid_user(bot, userid):
    useraid = bot.get_user(userid)
    if useraid:
        for x in range(100):
            try:
                await useraid.send("hehhe")
                print("[+] Message Sent")
            except:
                print("Unable To Raid User")


bot1 = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())


def get_user_input():
    g = input("""
▒█▀▀▄ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄
▒█░▒█ █▀▀ █░▀░█ █░░█ █░░█ 
▒█▄▄▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ▀░░▀

Made By Corlolex
___________________________________

[1] Mass Dm

Choice:""")



if g == '1':
    await raid_user(bot1, userid)
    
    
    
    
    
    
    
    
    
    
    bot1.run(tokens)

