import discord
import os
from discord.ext import commands
import google.generativeai as genai

token = "DISCORD BOT KEY"
geminiKey = "GEMINI API KEY"

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

genai.configure(api_key=geminiKey)

def count_letters(string):
    return len(string)
@bot.event

async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.command()
async def saveText(ctx, *, text):
    message = str(text)
    userName = ctx.author.name
    directory = './savedText/' 

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = f'{directory}{userName}.txt'

    if userName == f'{userName}.txt':
        with open(file_path, 'a') as file:
            file.write(message)
    else:
        with open(file_path, 'w') as file:
            file.write(message)

    await ctx.reply("Saved the text!")

@bot.command()
async def reciteText(ctx, *, text):
    recitedText = str(text)
    model = genai.GenerativeModel("gemini-1.5-flash")
    userName = ctx.author.name
    directory = './savedText/'
    file_path = f'{directory}{userName}.txt'
    with open(file_path, 'r') as file:
        savedText = file.read()
    response = model.generate_content("Compare the following 2 texts, " + str(savedText) + " this is the original text the author gave, now compare it to this which he remembered and give him a grade on his accuracy: " + recitedText)
    text_content = response.candidates[0].content.parts[0].text
    await ctx.reply(text_content)


bot.run(token)
