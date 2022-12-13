import locale
from datetime import datetime
import random
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from classes import CoinGeckoAPI
from os import getenv
from dotenv import load_dotenv

load_dotenv()
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

app = Client(
    'akacripto_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')


@app.on_message(filters.command('ajuda'))  # filters.photo / .voice / para fotos ou voz, posso concatenar com |
async def ajuda(client, message):
    await message.reply(
        'Menu de opções\n'
        'Use **/xinga** Para um Xingamento!\n'
        'Use **/bitcoin** para ver a cotação\n'
        'Use **/nome_da_altcoin** para ver a cotação\n'
    )


@app.on_message(filters.command('menu'))
async def menu_command(client, message):
    await message.reply(
        'Escolhe a opção',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['/ajuda', '/xinga'],
                ['/bitcoin', '/ethereum', 'kaspa']
            ],
            resize_keyboard=True
        ),
    )


@app.on_message(filters.command('xinga'))
async def xinga(client, message):
    arquivo = open("./xinga.txt", 'r', encoding="utf8")
    xinga_txt = arquivo.read()
    lista_xinga: list = xinga_txt.replace("\n", "").split(';')
    xingamento = random.choice(lista_xinga)
    await message.reply(xingamento)


@app.on_message()
async def messages(client, message):
    preco = ''
    atualizado_em = ''
    if api.ping():
        preco, atualizado_em = api.consulta_preco(message.text.replace("/", ""))
    data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
    cripto: str = message.text.replace("/", "")
    await message.reply(f'Cotação do {cripto.title()}\nU$ {preco}\nAtualizado em: {data_hora}')

print('running!!!')
app.run()
