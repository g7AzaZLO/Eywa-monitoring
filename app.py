import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from settings.config import TOKEN
from settings.const_messages import private
from handlers.handlers import router

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)


# Запуск бота
async def main() -> None:
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


asyncio.run(main())
