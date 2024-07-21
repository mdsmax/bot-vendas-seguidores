import disnake
import os
from disnake.ext import commands
import json

bot = commands.Bot()
with open("config.json") as file:
    config = json.load(file)
    token = config['token']
    owner = config['owner'] 
    hiperseguidoreskey = config['hiperseguidoreskey']
    mercadopagokey = config['mercadopagokey']
    logsCanal = config['canalLogs']
    comprasCanal = config['canalCompras']

bot.load_extension("commands.painel")
bot.load_extension("commands.botconfig")

@bot.event
async def on_ready():
    print("Bot iniciado")

bot.run(token)