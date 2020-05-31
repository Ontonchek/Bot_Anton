import discord
from discord.ext import commands

client = commands.Bot( command_prefix = 'Антон' )

#word
hello_words = [ 'Антон', 'антон', 'антох', 'Антох', 'Антончек', 'антончек', 'онтон', 'Онтон' ]
answer_words = [ 'Узнать информаницию о сервере', 'узнать информаницию о сервере', 'инфа', 'Инфа', 'Команды', 'команды'  ]


@client.event
async def on_ready():
	print( 'BOT connected' )

@client.event

async def on_message( message ):
	msg = message.content.lower()

	if msg in hello_words:
		await message.channel.send( 'Привет, чего хотел?' )

	if msg in answer_words:
		await message.channel.send( 'Пропиши в чат Антон хелп' )

# connect

token = open( 'token.txt', 'r' ).readline()

client.run( token )