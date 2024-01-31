import asyncio
import time
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from settings.const_messages import start_message, start_kb, check_sync_command, check_epoch_command, watchdog_status, \
    eywa_watchdog_already_started_message, sync_monitoring_alert_message, eywa_watchdog_stopped_message
from settings.config import TTS
from cmd import execute_command

router = Router()


# Обработка команды /start
@router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    await message.answer(text=start_message, reply_markup=start_kb)


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


# Обработка команды /start_eywa_watchdog
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
                await message.answer(sync_monitoring_alert_message + "\n\n" + result)
            if not watchdog_status:
                break
            time.sleep(TTS)
    else:
        await message.answer(eywa_watchdog_already_started_message)


# Обработка команды /stop_eywa_watchdog
@router.message(F.text.lower() == 'stop monitoring eywa synchronization')
@router.message(Command('stop_eywa_watchdog'))
async def stop_eywa_watchdog(message: types.Message) -> None:
    global watchdog_status
    watchdog_status = False
    await message.answer(eywa_watchdog_stopped_message)
