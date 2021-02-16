import discord
import asyncio

async def say(message, args : []):
    repeatCount = 1
    if len(args) < 1:
        return
    elif len(args) < 2:
        pass
    elif not args[1].isdigit():
        pass
    else:
        repeatCount = int(args[1])
    await message.delete()
    for i in range(0, repeatCount):
        await message.channel.send(args[0])
        await asyncio.sleep(0.5)

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