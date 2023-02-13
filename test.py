import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["!",""],intents=intents)
bot.remove_command("help")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if message.guild:
            CHANNEL_NAME = "聞き専","雑談"
            if message.channel.name in CHANNEL_NAME:
                print(f"{message.author.name} | {message.content}  ----{message.guild.name}メンバー数({message.guild.member_count})")
                file = open('index.html', 'a', encoding='UTF-8')
                for attachment in message.attachments:
                    if attachment.url.endswith(("png", "jpg", "jpeg")):
                        file.writelines(f"<nav><h1>{message.author.name}<span>{message.created_at}</span></h1><p>{message.content}</p><img src={attachment.url}><nav>\n")
                        file.close()

bot.run(Token)
