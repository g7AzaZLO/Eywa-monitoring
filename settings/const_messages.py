from aiogram.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton

# Сообщение для команды команды /start
start_message = "Eywa Monitoring Bot\n\nРазработчик - [G7]AzaZLO\nG7 Telegram - https://t.me/g7monitor"
eywa_watchdog_already_started_message = 'Watchdog already started'
sync_monitoring_alert_message = "Sync monitoring alert: node is not FULLY_SYNCED"
eywa_watchdog_started_message = "EYWA synchronization monitoring started"
eywa_watchdog_stopped_message = "Eywa synchronization monitoring is stopped"
eywa_started_stopping_message = "Start stopping monitoring eywa synchronization"
eywa_watchdog_already_stopped_message = "Watchdog already stopped"


# Команды которые прописываются в бота при его запуске
private = [
    BotCommand(command='sync', description='Check synchronization'),
    BotCommand(command='epoch', description='Check node hits in epochs'),
    BotCommand(command='start_eywa_watchdog', description='Start monitoring EYWA synchronization'),
    BotCommand(command='stop_eywa_watchdog', description='Stop monitoring EYWA synchronization'),
    BotCommand(command='check_current_epoch', description='Check current epoch')
]

# Клавиатура в тг
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Check synchronization'),
            KeyboardButton(text='Check node hits in epochs'),
        ],
        [
            KeyboardButton(text='Start monitoring EYWA synchronization'),
        ],
        [
            KeyboardButton(text='Stop monitoring EYWA synchronization'),
        ],
        [
            KeyboardButton(text='Check current epoch'),
        ],
    ],
    resize_keyboard=True,
)

# Команды
watchdog_status = False
check_sync_command = 'curl -s 127.0.0.1:8081/v1/sync_state|jq -r \'("NODE SYNC STATE: "+.result.state),((["CHAIN","SYNCED","DIFFS","sysDIFFS"] | (., map(length*"-"))),(.result.details|keys[] as $k |["\($k)", "\(.[$k].synced)", "\(.[$k].diffs.processedHeight)", "\(.[$k].diffs.sysProcessedHeight)"])|@tsv)\''
check_epoch_command = 'hostid=$(curl -s http://0.0.0.0:8081/v1/validator_info|jq -r .hostId);height=$(curl -s http://0.0.0.0:8081/v1/current_height|jq -r .result); for i in $(seq 1 $height); do result=$(curl -s -d chain_id=0 -d block_height=$i http://0.0.0.0:8081/v1/block|jq .events[].epochEvent.hostIds|grep $hostid); if [ -z $result ];then printf " $i "; else printf " ($i) ";fi;done;echo'
check_current_epoch_command = "curl -s -d chain_id=0 -d block_height=$(curl -s http://127.0.0.1:8081/v1/current_height|jq -r .result) http://127.0.0.1:8081/v1/block|jq -r '\"Current epoch: \" + .header.height, \"Epoch started: \" + (.header.timestamp|tonumber|strftime(\"%B %d %Y %I:%M %Z\"))'"