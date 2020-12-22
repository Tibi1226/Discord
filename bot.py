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
    print(TOKEN)

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
    if message.author.id == 418755604199243776:
        await message.channel.send("Ádám buta")

    #köszönés
    elif message.content == ('!hello') or message.content == ('!helló') or message.content == ('!szia') or message.content == ('!hi') or message.content == ('!üdv'):
        üdvözlés = random.choice(üdvözlések)
        print(üdvözlés)
        küldő =' {0.author.mention}!'.format(message)
        await message.channel.send(üdvözlés + küldő)

    #parancsok
    elif message.content == ('!help') or message.content == ('!info') or message.content == ('!botinfo') or message.content == ('!parancsok'):
        msg = """Tibi okosabb mint én
   !(bot)info, !parancsok, !help: Kiírja ezt az üzenetet.
   !tagok: Felsorolja a tagokat belépési sorrendben.
   !sad, !kár, !szomorú: Zétény éltal ihletve
   !kakilniakarok, !szarniakarok, !iwanttopoo: Zétény által ihletve"""
        await message.channel.send(msg)


    elif message.content == ('!tagok'):
        await message.channel.send('- ' + members)


    elif message.content == ('!kár') or message.content == ('!sad') or message.content == ('!szomorú'):
        await message.channel.send('Sajnálom... (⌣́_⌣̀) ')


    elif message.content == ('!kakilniakarok') or message.content == ('!szarniakarok') or message.content == ('!iwanttopoo'):
        await message.channel.send('Nemááá....  💩')






client.run('NzE0Mzc3MjU4Mzc4NDYxMjQ1.'+'Xstxqg.B0tSyT1rcwF6NyE6JdxwqLOFNLM')
