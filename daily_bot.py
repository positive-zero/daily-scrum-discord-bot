import os
import discord
import random
import time
import datetime

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$daily'):
        print(f'Daily requested at: {datetime.datetime.now()}')

        members = []
        members = [member for member in client.get_all_members()
                   if member != client.user]
        random.shuffle(members)

        daily_ordering = 'The daily ordering will be:\n\n'
        for member in members:
            if os.environ.get('ROLE', 'daily participant') in [role.name for role in member.roles]:
                daily_ordering += f'- {member.mention}\n'
        await message.channel.send(daily_ordering)

        await message.channel.send('15 minutes remaining...\n')
        for minutes in [1, 2, 3]:
            if minutes == 2:
                await message.channel.send('10 minutes remaining...\n')
            if minutes == 3:
                await message.channel.send('5 minutes remaining...\n')

            time.sleep(60 * 5)  # 5 minutes

        await message.channel.send('The time is up.')


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(os.environ['TOKEN'])
