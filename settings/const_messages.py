from aiogram.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton

# Сообщение для команды команды /start
start_message = "Eywa Monitoring Bot\n\nРазработчик - [G7]AzaZLO\nG7 Telegram - https://t.me/g7monitor"
eywa_watchdog_already_started_message = 'Watchdog already started'
sync_monitoring_alert_message = "Sync monitoring alert: node is not FULLY_SYNCED"
eywa_watchdog_stopped_message = "Eywa synchronization monitoring is stopped"

# Команды которые прописываются в бота при его запуске
private = [
    BotCommand(command='sync', description='Check synchronization'),
    BotCommand(command='epoch', description='Check node hits in epochs'),
    BotCommand(command='start_eywa_watchdog', description='Start EYWA synchronization monitoring')
]

# Клавиатура в тг
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Check synchronization'),
            KeyboardButton(text='Check node hits in epochs'),
            KeyboardButton(text='Start EYWA synchronization monitoring'),
        ],
    ],
    resize_keyboard=True,
)

# Команды
watchdog_status = False
check_sync_command = 'curl -s 127.0.0.1:8081/v1/sync_state|jq -r \'("NODE SYNC STATE: "+.result.state),((["CHAIN","SYNCED","DIFFS","sysDIFFS"] | (., map(length*"-"))),(.result.details|keys[] as $k |["\($k)", "\(.[$k].synced)", "\(.[$k].diffs.processedHeight)", "\(.[$k].diffs.sysProcessedHeight)"])|@tsv)\''
check_epoch_command = 'hostid=$(curl -s http://0.0.0.0:8081/v1/validator_info|jq -r .hostId);height=$(curl -s http://0.0.0.0:8081/v1/current_height|jq -r .result); for i in $(seq 1 $height); do result=$(curl -s -d chain_id=0 -d block_height=$i http://0.0.0.0:8081/v1/block|jq .events[].epochEvent.hostIds|grep $hostid); if [ -z $result ];then printf " $i "; else printf " ($i) ";fi;done;echo'
