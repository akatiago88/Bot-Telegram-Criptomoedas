# from pyrogram.types import ReplyKeyboardMarkup
# CRIA UM TECLADO VIRTUAL DENTRO DO TELEGRAM
# @app.on_message(filters.command('teclado'))
# async def teclado(client, message):
#     teclado = ReplyKeyboardMarkup(
#         [
#             ['/ajuda', '/xinga'],
#             ['/bitcoin', '/ethereum', 'kaspa']
#         ],
#         resize_keyboard=True)
#     await message.reply(
#         'Aperta ai no teclado',
#         reply_markup=teclado,
#     )
# -------------------------------------------------
# @app.on_message(filters.command('photo'))
# async def photo(client, message):
#     await app.send_photo(
#         message.chat.id,
#         'https://site.com/photo.jpg'
#     )
# ---------------------------------------------------
# on_edited_message()
# on_deleted_message()
