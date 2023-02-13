def emoji(content):
    content = content.encode('utf-8', 'ignore').decode('utf-8')
    return content


def msg_process(msg):
    urls = [x.url for x in msg.attachments]
    author = emoji(str(msg.author))
    content = emoji(str(msg.content))
    channel = emoji(str(msg.channel))
    guild = emoji(str(msg.guild.name))
    return urls, author, content, channel, guild
