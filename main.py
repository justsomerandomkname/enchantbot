import os
os.system('git init')
os.system('git add .')
import random
import discord
import os
import time
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content == 'makeEXE':

            response2 = await bot.send_file(bot.message.channel, open('maker.py'))
            await bot.say(response2)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    random_number = random.randint(10000)
    if message.content == 'randomNumber':
        response = random.choice(random_number)
        await bot.say(response)

        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')

            # bans a user with a reason

            # this was in a cog
            # The below code bans player.

        @client.event
        @commands.has_permissions(ban_members=True)
        async def ban(self, ctx, member: discord.Member, *, reason=None):
            await member.ban(reason=reason)
            await bot.send(f'User {member} has been kicked')

    # The below code unbans player.
    @client.event
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await bot.guild.unban(user)
                await bot.send(f'Unbanned {user.mention}')
                return


# The below code kicks player
@client.event
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason):
    await member.kick(reason=reason)
    await bot.send(f'User {member} has been kick')

    @bot.command(pass_context=True)
    async def mute(ctx, user_id, userName: discord.User):
        if ctx.message.author.server_permissions.administrator:
            user = ctx.message.author
            role = discord.utils.get(user.server.roles, name="Muted")
            await client.add_roles(user, role)
        else:
            embed = discord.Embed(title="Permission Denied.",
                                  description="You don't have permission to use this command.", color=0xff00f6)
            await bot.say(embed=embed)



    client.run(TOKEN)
