Bot para o Telegram com comandos para retornar cotação de criptomoedas, funciona no privado e em grupo.

no main.py

api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
    
Você vai trocar pela suas credências, as duas primeiras você pega no site do Telegram após fazer login com verificação da sua conta, o terceiro (bot_token) é o token fornecido pelo bot father ao concluir a criação do bot.
obs.: Utitlizei o getenv e o dotenv para ocultar as minhas credênciais, caso não for usa-las pode retirar essas bibliotecas.

ex.:
api_id="43424234"
api_hash="f54w2f5ef4w5f4"
bot_token="3f245324r3f5r34f"
