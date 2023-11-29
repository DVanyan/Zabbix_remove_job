import paramiko
import os

credential_ids = ['ansible_svc', 'jenkins_svc-digi.loc']

def try_to_connect(server, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username=username, password=password)
        return True
    except paramiko.AuthenticationException:
        return False
    finally:
        ssh.close()

def connect_to_server(server):
    for credential_id in credential_ids:
        # Получение логина и пароля
        username = os.getenv(f'USERNAME_{credential_id}')
        password = os.getenv(f'PASSWORD_{credential_id}')

        # Попытка подключения к серверу
        success = try_to_connect(server, username, password)

        if success:
            return username, password
    return None, None



def remove_programs_from_servers(servers, program_name):
    for server in servers:
        remove_program(server, program_name)
        
# Получаем список серверов из переменной окружения
servers_str = os.getenv('Servers')

# Преобразуем строку в список
servers = servers_str.split(', ')

# Запуск удаления приложения на нескольких серверах
remove_programs_from_servers(servers, 'zabbix-agent')