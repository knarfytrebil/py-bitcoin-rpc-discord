import simplejson as json
import logging
import discord
from discord.ext import commands
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from settings import RPC_URL, DISCORD_PREFIX, DISCORD_CODE_TEMPLATE, DISCORD_TOKEN, DISCORD_JSON_FORMAT

logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

rpc_connection = AuthServiceProxy(RPC_URL)
bot = commands.Bot(command_prefix=DISCORD_PREFIX)

def format_code(_dict, language="javascript"):
    return DISCORD_CODE_TEMPLATE.format(
        json.dumps(_dict, **DISCORD_JSON_FORMAT),
        language,
    )

@bot.command()
async def blockchaininfo(ctx):
    res = rpc_connection.getblockchaininfo()
    formated = format_code(res)
    await ctx.send(formated)

@bot.command()
async def bestblockhash(ctx):
    res = rpc_connection.getbestblockhash()
    formated = format_code(res)
    await ctx.send(formated)

bot.run(DISCORD_TOKEN)


