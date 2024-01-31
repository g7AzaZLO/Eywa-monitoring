import subprocess


# Функция для выполнения команды на сервере и получения результата
def execute_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return result.stdout.decode('utf-8')
    else:
        return result.stderr.decode('utf-8')
