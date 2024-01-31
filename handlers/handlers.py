import asyncio
import time
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from settings.const_messages import start_messages, start_kb, check_sync_command, check_epoch_command, watchdog_status, \
    watchdog_already_started_messages
from settings.config import TTS
from cmd import execute_command

router = Router()


# Обработка команды /start
@router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    await message.answer(text=start_messages, reply_markup=start_kb)


# Обработка команды /sync
@router.message(F.text.lower() == 'check synchronization')
@router.message(Command('sync'))
async def check_sync(message: types.Message) -> None:
    result = execute_command(check_sync_command)
    await message.answer(result)


# Обработка команды /epoch
@router.message(F.text.lower() == 'check node hits in epochs')
@router.message(Command('epoch'))
async def check_epoch(message: types.Message) -> None:
    result = execute_command(check_epoch_command)
    await message.answer(result)

# Обработка команды по запуску мониторинга
@router.message(F.text.lower() == 'start eywa synchronization monitoring')
@router.message(Command('start_eywa_watchdog'))
async def start_eywa_watchdog(message: types.Message) -> None:
    global watchdog_status
    if not watchdog_status:
        watchdog_status = True
        await message.answer("EYWA synchronization monitoring started")
        while True:
            result = execute_command(check_sync_command)
            if "FULLY_SYNCED" in result:
                continue
            else:
                await message.answer("Sync monitoring alert: node is not FULLY_SYNCED" + "\n\n" + result)
            if not watchdog_status:
                break
            time.sleep(TTS)
    else:
        await message.answer(watchdog_already_started_messages)
