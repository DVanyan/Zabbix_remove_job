from pypsexec.client import Client
import os

# Получаем имя или IP-адрес удаленного хоста из переменных окружения
remote_host = os.getenv("Servers")

# Получаем логин и пароль из Jenkins
username = os.getenv("windows_user")
password = os.getenv("windows_pass")

# Создаем клиента PsExec
c = Client(remote_host + '.digi.loc', username=username, password=password)

# Подключаемся к удаленной машине
c.connect()

# Создаем новую сессию PowerShell и выполняем команду "ping"
c.create_service()
stdout, stderr, rc = c.run_executable("cmd.exe", arguments="/c ping 8.8.8.8")

# Выводим результат
print(stdout)

# Закрываем соединение
c.remove_service()
c.disconnect()
