import discord
import asyncio
import classpectar
import checker
import json
import re
from discord.ext import commands

cooldowns_ativos = {}
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

BOT_TOKEN = config.get('BOT_TOKEN')


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


@bot.event
async def on_message(message):
    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)
        return
    if message.author == bot.user:
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
        if not cooldowns_ativos[guild_id]:
            primeira_sequencia = ' '.join(sequencias_encontradas[0])
            await message.channel.send(f"{primeira_sequencia} é um nome valido")

    if 'jeff' in message.content:
        if not cooldowns_ativos[guild_id]:
            await message.channel.send(
                "https://tenor.com/view/homestuck-sbahj-hella-jeff-sweet-bro-sweet-bro-and-hella-jeff-gif-26224202")

    words = message.content.lower().split()
    if not cooldowns_ativos[guild_id]:
        for word in words:
            if re.search(r'\bbro\b', word):
                await message.channel.send(
                    "https://tenor.com/view/i-told-you-about-the-stairs-i-warned-you-about-the-stairs-stairs-i"
                    "-told-you"
                    "-gif-21854458")

        if message.content == 'liv apresente-se':
            await message.channel.send(
                "Handle: Liv Tyler\nClasspect: Seer of Light\nMaior de idade: 🤖\nPronomes: Ela/Dela")

    await bot.process_commands(message)


@bot.command()
async def classpect(ctx, arg1, arg2):
    await ctx.send(classpectar.fazer_classpect(arg1, arg2))


bot.run(BOT_TOKEN)
