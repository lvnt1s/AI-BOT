from aiocryptopay import AioCryptoPay, Networks
import asyncio
from core.config_reader import settings



async def create_cryptobot_invoice(amount):
    async with AioCryptoPay(token=settings.CRYPTOBOT_TOKEN, network=Networks.MAIN_NET) as engine:
        amount = await engine.get_amount_by_fiat(summ=amount, asset='USDT', target='RUB')
        invoice = await engine.create_invoice(asset='USDT', amount=amount)
        return invoice.bot_invoice_url


# async def check_invoice(summ, id_pay):
#     engine = AioCryptoPay(token=settings.CRYPTOBOT_TOKEN, network=Networks.MAIN_NET)
#     old_invoice = await engine.get_invoices(invoice_ids=id_pay)
#     return old_invoice[0].status


