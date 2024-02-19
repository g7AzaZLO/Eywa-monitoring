import asyncio
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from settings.const_messages import start_message, start_kb, check_sync_command, check_epoch_command, watchdog_status, \
    eywa_watchdog_already_started_message, sync_monitoring_alert_message, eywa_watchdog_stopped_message, \
    eywa_watchdog_started_message, eywa_started_stopping_message, eywa_watchdog_already_stopped_message, \
    check_current_epoch_command, check_bridge_version_command
from settings.config import TTS
from cmd import execute_command

router = Router()


# Обработка команды /start
@router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    print("Processing /start command")
    await message.answer(text=start_message, reply_markup=start_kb)


# Обработка команды /sync
@router.message(F.text.lower() == 'check synchronization')
@router.message(Command('sync'))
async def check_sync(message: types.Message) -> None:
    print("Processing /check_sync command")
    result = execute_command(check_sync_command)
    await message.answer(result)


# Обработка команды /epoch
@router.message(F.text.lower() == 'check node hits in epochs')
@router.message(Command('epoch'))
async def check_epoch(message: types.Message) -> None:
    print("Processing /epoch command")
    result = execute_command(check_epoch_command)
    await message.answer(result)


# Обработка команды /start_eywa_watchdog
@router.message(F.text.lower() == 'start monitoring eywa synchronization')
@router.message(Command('start_eywa_watchdog'))
async def start_eywa_watchdog(message: types.Message) -> None:
    print("Processing /start_eywa_watchdog command")
    global watchdog_status
    if not watchdog_status:
        watchdog_status = True
        print("set watchdog_status = True")
        await message.answer(eywa_watchdog_started_message)
        while True:
            print("check sync in watchdog")
            result = execute_command(check_sync_command)
            if not watchdog_status:
                print("stop watchdog in while true")
                await message.answer(eywa_watchdog_stopped_message)
                break
            if "FULLY_SYNCED" in result:
                print("watchdog say 'all good'")
                print("start sleep")
                await asyncio.sleep(TTS)
                print("continue")
                continue
            else:
                print("watchdog say anything is bad")
                await message.answer(sync_monitoring_alert_message + "\n\n" + result)
                print("start sleep")
                await asyncio.sleep(TTS)
                print("continue")
    else:
        await message.answer(eywa_watchdog_already_started_message)


# Обработка команды /stop_eywa_watchdog
@router.message(F.text.lower() == 'stop monitoring eywa synchronization')
@router.message(Command('stop_eywa_watchdog'))
async def stop_eywa_watchdog(message: types.Message) -> None:
    print("Processing /stop_eywa_watchdog command")
    global watchdog_status
    if watchdog_status:
        watchdog_status = False
        await message.answer(eywa_started_stopping_message)
    else:
        await message.answer(eywa_watchdog_already_stopped_message)

# Обработка команды /check_current_epoch
@router.message(F.text.lower() == 'check current epoch')
@router.message(Command('check_current_epoch'))
async def check_current_epoch(message: types.Message) -> None:
    print("Processing /check_current_epoch command")
    result = execute_command(check_current_epoch_command)
    await message.answer(result)

# Обрабтка команды /check_bridge_version
@router.message(F.text.lower() == 'check bridge version')
@router.message(Command('check_bridge_version'))
async def check_current_epoch(message: types.Message) -> None:
    print("Processing /check_bridge_version command")
    result = execute_command(check_bridge_version_command)
    await message.answer(result)
