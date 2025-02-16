import os
import discord
from discord.ext import commands
import wavelink

# Fetch bot token from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.loop.create_task(connect_nodes())

async def connect_nodes():
    """Connect to Lavalink nodes"""
    await bot.wait_until_ready()
    node = wavelink.Node(uri="localhost:2333", password="youshallnotpass")
    await wavelink.Pool.connect(client=bot, nodes=[node])

@bot.command()
async def join(ctx):
    """Bot joins the voice channel"""
    if ctx.author.voice:
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        await ctx.send("Joined voice channel!")
    else:
        await ctx.send("Join a voice channel first!")

@bot.command()
async def play(ctx, *, query: str):
    """Play a song from YouTube"""
    vc: wavelink.Player = ctx.voice_client
    if not vc:
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)

    tracks = await wavelink.YouTubeTrack.search(query)
    if not tracks:
        await ctx.send("No results found.")
        return

    await vc.play(tracks[0])
    await ctx.send(f"Now playing: {tracks[0].title}")

@bot.command()
async def leave(ctx):
    """Disconnect the bot"""
    vc = ctx.voice_client
    if vc:
        await vc.disconnect()
        await ctx.send("Disconnected from voice channel.")

# Run the bot with the environment variable token
bot.run(TOKEN)

