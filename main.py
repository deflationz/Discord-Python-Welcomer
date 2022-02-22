import discord
from discord.ext import commands
token = "Token Here"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '%', intents = intents)
client.remove_command("help")

def simpleEmbed(s):
	embed = discord.Embed(
	    color=discord.Colour.green(),
	    description=s,
	)
	return embed

@client.event
async def on_ready():
	activity = discord.Activity(name="DeflationzWare", type=1)
	await client.change_presence(status=discord.Status.online, activity=activity)
	print("Bot online.")
@client.event
async def on_member_join(member):
	channel = client.get_channel(922379989343699014)
	embed = discord.Embed(title= f"Welcome to **{member.guild.name}**", description= f"Welcome to DeflationzWare! {member.mention}! Hope you enjoy our scripts + community!", colour = discord.Colour.blue())
	embed.set_footer(text = "DeflationzWare")
	embed.set_thumbnail(url = member.avatar_url)
	await channel.send(embed = embed)
@client.event
async def on_member_remove(member):
    channel = client.get_channel(922379989343699014)
    embed=discord.Embed(title="Goodbye!", description=f"{member.mention}just left the {member.guild.name}, hope to see you again, {member.display_name}!", color=0xffffff)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(text = "DeflationzWare")
    await channel.send(embed=embed)


client.run(token)
