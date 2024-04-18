import discord
import random
import asyncio
from discord.ext import commands

# Define the list of words for the game
word_list = ["apple", "banana", "orange", "grape", "strawberry", "watermelon"]

# Create a bot instance
bot = commands.Bot(command_prefix='!')
cooldown_time = 10  # Cooldown time between guesses in seconds

# Dictionary to store user scores
user_scores = {}

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command: Start the game
@bot.command()
async def start(ctx):
    # Choose a random word from the word list
    chosen_word = random.choice(word_list)
    
    # Send a message to start the game
    await ctx.send(f"Guess the word! It has {len(chosen_word)} letters. Type your guess in the chat.")

    # Function to check if the message content is the correct word
    def check(msg):
        return msg.content.lower() == chosen_word and msg.channel == ctx.channel and msg.author != bot.user

    # Wait for a correct guess
    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
        await ctx.send(f"Congratulations! {msg.author.mention} guessed the word correctly: {chosen_word}")
        
        # Update user score
        if msg.author.id in user_scores:
            user_scores[msg.author.id] += 1
        else:
            user_scores[msg.author.id] = 1
    except asyncio.TimeoutError:
        await ctx.send("Time's up! The word was: " + chosen_word)

# Command: Get user score
@bot.command()
async def score(ctx):
    if ctx.author.id in user_scores:
        await ctx.send(f"Your score is: {user_scores[ctx.author.id]}")
    else:
        await ctx.send("You haven't played any games yet.")

# Command: Get hint for the word
@bot.command()
async def hint(ctx):
    if ctx.author.id in user_scores:
        chosen_word = random.choice(word_list)
        hint = f"The word has {len(chosen_word)} letters."
        await ctx.send(hint)
    else:
        await ctx.send("You haven't played any games yet.")

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
