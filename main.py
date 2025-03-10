import discord
import asyncio
import checker
import json
import re

cooldowns_ativos = {}

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
BOT_TOKEN = config.get('BOT_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        guild_id = message.guild.id
        if guild_id not in cooldowns_ativos:
            cooldowns_ativos[guild_id] = False

        if message.content == "liv cooldown":
            if guild_id not in cooldowns_ativos:
                cooldowns_ativos[guild_id] = False

            cooldowns_ativos[guild_id] = not cooldowns_ativos[guild_id]
            status = "ativados" if cooldowns_ativos[guild_id] else "desativados"
            await message.channel.send(f"Cooldowns foram {status} para este servidor.")
        
        sequencias_encontradas = checker.detectar_nomes(message.content)
        if sequencias_encontradas:
            if cooldowns_ativos[guild_id] == False:
                primeira_sequencia = ' '.join(sequencias_encontradas[0])
                await message.channel.send(f"{primeira_sequencia} é um nome valido")
    
        if 'jeff' in message.content:
            if cooldowns_ativos[guild_id] == False:
                await message.channel.send(
                    "https://tenor.com/view/homestuck-sbahj-hella-jeff-sweet-bro-sweet-bro-and-hella-jeff-gif-26224202")
              
        words = message.content.lower().split()
        if cooldowns_ativos[guild_id] == False:
            for word in words:
                if re.search(r'\bbro\b', word):
                    await message.channel.send(
                    "https://tenor.com/view/i-told-you-about-the-stairs-i-warned-you-about-the-stairs-stairs-i-told-you"
                    "-gif-21854458")

        if message.content == 'liv apresente-se':
            await message.channel.send("Handle: Liv Tyler\nClasspect: Seer of Light\nMaior de idade: 🤖\nPronomes: Ela/Dela")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(BOT_TOKEN)
