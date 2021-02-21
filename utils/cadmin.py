import discord
import asyncio

async def say(message, args : []):
    repeatCount = 1
    content : str

    if not args or len(args) < 1:
        message.channel.send("Can't dend empty message")

    if len(args) < 2:
        content = args[0]
    elif args[0].isdigit():
        repeatCount = int(args[0])
        content = args[1]
    elif args[1].isdigit():
        repeatCount = int(args[1])
        content = args[0]
    else:
        content = args[0]

    if len(content) > 2000:
        content = content[0, 2000]

    await message.delete()
    for i in range(0, repeatCount):
        await message.channel.send(content)
        await asyncio.sleep(0.7)

async def clear(message, args : []) -> int:
    amount : int
    channel = message.channel
    await message.delete()
    if len(args) > 0 and args[0].isdigit():
        amount = int(args[0])
    else:
        amount = 10
    deles = await channel.purge(limit = amount)
    return len(deles)