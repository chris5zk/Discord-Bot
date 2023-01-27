import os
import log
import time
import discord
import response


async def send_message(message, user_message, is_private):
    try:
        res = response.handle_response(user_message)
        await message.author.send(res) if is_private else await message.channel.send(res)
    except Exception as e:
        print(e)


def run_discord_bot(token, full, chat):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # logger of full log dict and file
    filename = time.strftime('%Y-%m-%d')
    os.makedirs(f'{full}/', exist_ok=True)
    log_path = f'{full}/{filename}.log'
    log.full_log(log_path)

    # guild & logger check
    guild_set = set()
    logger_dict = {}

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Alert!!! Didn't check the bot message loop yet!!!

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        guild = str(message.guild.name)

        # build logger for each guild
        if guild not in guild_set:
            guild_set.add(guild.encode('unicode-escape', 'ignore').decode('unicode-escape'))
            os.makedirs(f'./{chat}/{guild}/', exist_ok=True)
            chat_path = f'{chat}/{guild}/{filename}.log'
            chat_logger = log.chat_log(chat_path, guild)
            logger_dict[guild] = chat_logger

        # write to log file
        chat_str = f'[{channel}]{username}: {user_message}'
        logger_dict[guild].info(chat_str.encode('unicode-escape', 'ignore').decode('unicode-escape'))

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(token, log_handler=None)
