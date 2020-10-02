# bot.py

import random
import os
import discord
from dotenv import load_dotenv

üdvözlések = ['Szia', 'Üdv', 'Helló']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()


#Szerver kapcsolat, tagok kiírása
@client.event
async def on_ready():
    global guild
    guild = discord.utils.get(client.guilds, name=GUILD)
    global members
    members = '\n - '.join([member.name for member in guild.members])
    print(
        f'{client.user} csatlakozott a következő szerverhez:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print(f'Szerver tagok:\n - {members}')

#Új tagok üdvözlése
@client.event
async def on_member_join(member):
    members = '\n - '.join([member.name for member in guild.members])
    await member.create_dm()
    await member.dm_channel.send(
        f'Szia, {member.name}, én Zeta klónja vagyok, egy bot a szerveren.\nÍrd be, hogy !info, hogy megismerd a képességeimet.'
    )


@client.event
async def on_message(message):
    #Ha saját maga írta, nem válaszol
    if message.author == client.user:
        return

    #köszönés
    if message.content == ('!hello') or message.content == ('!helló') or message.content == ('!szia') or message.content == ('!hi') or message.content == ('!üdv'):
        üdvözlés = random.choice(üdvözlések)
        print(üdvözlés)
        küldő =' {0.author.mention}!'.format(message)
        await message.channel.send(üdvözlés + küldő)

    #parancsok
    if message.content == ('!help') or message.content == ('!info') or message.content == ('!botinfo') or message.content == ('!parancsok'):
        msg = """Üdv, én Zeta klónja vagyok.
\nNéhány hasznos dolgot tudok, mint taco-t adni az embereknek, vagy kiírni ezt a szöveget.
\nParancsok:
   !(bot)info, !parancsok, !help: Kiírja ezt az üzenetet.
   !tagok: Felsorolja a tagokat belépési sorrendben.
   !sad, !kár, !szomorú: Zétény éltal ihletve
   !kakilniakarok, !szarniakarok, !iwanttopoo: Zétény által ihletve
   !taco <mennyiség> <címzett>: BÉTA!!* Taco küldésével kifejezheted az elismerésedet valaki iránt.
    Egyszerre 1-5 taco-t adhatsz egy embernek. Példa: !taco 3 @Pistabácsi13
    Márta Nénihez a !help_márta_néni szükségeltetik beírni.

    *nem létezik"""
        await message.channel.send(msg)


    if message.content == ('!tagok'):
        await message.channel.send('- ' + members)


    if message.content == ('!kár') or message.content == ('!sad') or message.content == ('!szomorú'):
        await message.channel.send('Sajnálom... (⌣́_⌣̀) ')


    if message.content == ('!kakilniakarok') or message.content == ('!szarniakarok') or message.content == ('!iwanttopoo'):
        await message.channel.send('Nemááá....  💩')






client.run(TOKEN)
