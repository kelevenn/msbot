import discord
from discord import app_commands
from discord.ext import commands
import random
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
print(os.getenv("TOKEN"))
bot = commands.Bot(command_prefix='!')

q_count_3s = 0 
q_count_2s = 0 
q_count_1s = 0

q_users_3s = []
q_users_2s = []
q_users_1s = []

id_do_servidor = 1257121738383167601
channel_3s = 1257180622254768128
channel_2s = 1257180496090370179
channel_1s = 1257180378226102293

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=id_do_servidor)) 
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'convitems', description='Link de convite para Main Scrim')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://discord.gg/eZNCgkUUWq", ephemeral = False) 


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Teste pro bot, caso tenha alguma resposta está funcionando.')
async def slash3(interaction: discord.Interaction):
    await interaction.response.send_message(f"Opa", ephemeral = True) 


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'numero', description='Número aleatório de 1 a 100')
async def slash4(interaction: discord.Interaction):
    numero = random.randint(1,100)
    await interaction.response.send_message(f" {numero} ", ephemeral = False) 


@bot.command()
async def q(ctx):
    global q_count_3s, q_count_2s, q_count_1s
    global q_users_3s, q_users_2s, q_users_1s

    if ctx.channel.id == channel_3s:
        q_count_3s += 1
        q_users_3s.append(ctx.author.mention)
        if q_count_3s == 1:
            await ctx.send('@everyone, +5')
        elif q_count_3s == 2:
            await ctx.send('@everyone, +4')
        elif q_count_3s == 3:
            await ctx.send('@everyone, +3')
        elif q_count_3s == 4:
            await ctx.send('@everyone, +2')
        elif q_count_3s == 5:
            await ctx.send('@everyone, +1!')
        elif q_count_3s == 6:
            mentions = ', '.join(q_users_3s)
            await ctx.send(f'{mentions} queue completed.')
            q_count_3s = 0
            q_users_3s = []
    elif ctx.channel.id == channel_2s:
        q_count_2s += 1
        q_users_2s.append(ctx.author.mention)
        if q_count_2s == 1:
            await ctx.send('@everyone, +3')
        elif q_count_2s == 2:
            await ctx.send('@everyone, +2')
        elif q_count_2s == 3:
            await ctx.send('@everyone, +1!!')
        elif q_count_2s == 4:
            mentions = ', '.join(q_users_2s)
            await ctx.send(f'{mentions} queue completed.')
            q_count_2s = 0
            q_users_2s = []
    elif ctx.channel.id == channel_1s:
        q_count_1s += 1
        q_users_1s.append(ctx.author.mention)
        if q_count_1s == 1:
            await ctx.send('@everyone, +1')
        elif q_count_1s == 2:
            mentions = ', '.join(q_users_1s)
            await ctx.send(f'{mentions} queue completed.')
            q_count_1s = 0
            q_users_1s = []
    else:
        await ctx.send('O comando queue apenas funciona em chats específicos!')


      

aclient.run(os.getenv("TOKEN"))