import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

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
    while True:
        dmVagyNem = input("DM?")
        bool(dmVagyNem)

        if dmVagyNem:
            print("Direct message\n")
            userId = int(input("Felhasználó id-je?"))
            user = await client.fetch_user(userId)
            if bool(input("Neki szeretnéd küldeni? "+ user.display_name + "(True/False)")):
                await user.send(input("Üzenet:"))

        
        else:
            print("Üzenet a szerveren\n")
            channel = client.get_channel(714393659038105655)
            await channel.send(input("Üzenet:"))




client.run('NzE0Mzc3MjU4Mzc4NDYxMjQ1.'+'Xstxqg.B0tSyT1rcwF6NyE6JdxwqLOFNLM')