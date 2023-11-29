import paramiko
import os

os_type = "none"
credential_ids = ['ansible_svc', 'jenkins_svc-digi.loc']

def try_to_connect(server, credential_ids):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for credential_id in credential_ids:
        # Получение логина и пароля
        username = os.getenv(f'USERNAME_{credential_id}')
        password = os.getenv(f'PASSWORD_{credential_id}')

        try:
            ssh.connect(server, username=username, password=password)
            return 'Linux'
        except paramiko.AuthenticationException:
            continue  # Если подключение не удалось, переходим к следующему набору учетных данных
        finally:
            ssh.close()
    return 'Windows'  # Если ни одно подключение не удалось, возвращаем 'Windows'


# Получаем список серверов из переменной окружения
servers_str = os.getenv('Servers')

# Преобразуем строку в список
for i in servers_str:
    if len(servers_str) == 1:
        servers = servers_str
    else:
        servers = servers_str.split(', ')

def remove_programs_from_servers(servers, program_name):
    for server in servers:
        connect_to_server(server)
