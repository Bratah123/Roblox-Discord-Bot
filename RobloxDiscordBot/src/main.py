import time
from discord.ext import commands

from src import Util
from src.commands import Commands
from src.settings import Config

t0 = time.time()  # Getting the time the program starts so we can time how long the bot takes to load

client = commands.Bot(command_prefix=Config.PREFIX)

commands = {
    f"{Config.PREFIX}help": Commands.help_command,

    f"{Config.PREFIX}profile": Commands.roblox_profile,
    f"{Config.PREFIX}roblox": Commands.roblox_profile,

    f"{Config.PREFIX}profileid" : Commands.profile_id,

    f"{Config.PREFIX}searchname": Commands.search_username
}


@client.event
async def on_ready():
    print("[DONE] Bot is now online.")
    t1 = time.time()
    print(f"[DONE] Successfully loaded bot in {t1 - t0} seconds")


@client.event
async def on_message(ctx):
    msg_content = ctx.content.lower()
    args = msg_content.split(" ")
    if ctx.author is client.user:  # check if the user is a bot
        return
    if args[0] in commands:
        func = commands.get(args[0], lambda: 'Invalid')(ctx, args)
        if Util.is_embed_message(args[0]):
            await ctx.channel.send(embed=func)
        if not Util.is_embed_message(args[0]):
            await ctx.channel.send(func)
        print(f"[LOGS] {ctx.author.name} used {args[0]} command.")


def main():
    client.run(Config.TOKEN)


if __name__ == '__main__':
    main()
