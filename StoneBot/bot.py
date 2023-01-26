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

    filename = time.strftime('%Y-%m-%d')
    log_path = f'{full}/{filename}.log'
    chat_path = f'{chat}/{filename}.log'
    log.full_log(log_path)
    chat_logger = log.chat_log(chat_path)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        chat_str = f'[{channel}]{username}: {user_message}'
        chat_logger.info(chat_str.encode('unicode-escape', 'ignore').decode('unicode-escape'))

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(token, log_handler=None)
