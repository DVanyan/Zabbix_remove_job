import paramiko
import os

def connect_to_server(server_name):
    for credential_id in credential_ids:
        # Получение логина и пароля
        username = os.getenv(f'USERNAME_{credential_id}')
        password = os.getenv(f'PASSWORD_{credential_id}')

        # Попытка подключения к серверу
        success = try_to_connect(server_name, username, password)

        if success:
            return username, password
    return None, None

def remove_program(server_ip, username, password, program_name):
    try:
        # Создаем SSH-клиент
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Подключаемся к серверу
        ssh_client.connect(server_ip, username=username, password=password)

        # Определяем команду для удаления программы в зависимости от операционной системы
        _, stdout, _ = ssh_client.exec_command('uname')
        os_type = stdout.read().decode().strip()

        if os_type == 'Linux':
            command = f'sudo apt-get remove {program_name}'  # Пример команды для Ubuntu/Debian
        elif os_type == 'Linux':
            command = f'sudo yum remove {program_name}'
        elif os_type == 'Windows':
            command = f'wmic product where "name=\'{program_name}\'" call uninstall'  # Команда для удаления программы на Windows
        else:
            print('Данная операционная система не поддерживается.')
            return

        # Выполняем команду для удаления программы
        _, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode().strip()

        if output:
            print(f'Результат выполнения команды: {output}')
        else:
            print(f'Программа {program_name} успешно удалена.')
    except paramiko.AuthenticationException:
        print('Ошибка аутентификации. Проверьте правильность имени пользователя и пароля.')
    except paramiko.SSHException as e:
        print(f'Ошибка подключения к серверу: {str(e)}')
    finally:
        # Закрываем SSH-соединение
        ssh_client.close()

def remove_programs_from_servers(servers, username, password, program_name):
    for server in servers:
        remove_program(server, username, password, program_name)

# Запуск удаления приложения на нескольких серверах
servers = ['192.168.1.100', '192.168.1.101', '192.168.1.102']
remove_programs_from_servers(servers, 'username', 'password', 'zabbix-agent')