import paramiko
import os

os_type = "none"

def try_to_connect(server):
    server = server + '.digi.loc'
    print(server)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Получение логина и пароля
    username = os.getenv('jenkins_user')
    password = os.getenv('jenkins_pass')

    try:
        ssh.connect(server, username=username, password=password)
        
        # Выполнение команды uname -a
        stdin, stdout, stderr = ssh.exec_command("uname -a")
        output = stdout.read().decode()
        linux_type = output.split()  # Чтение вывода команды
                
        return linux_type  # Возвращаем тип Linux
    except Exception as e:  # Обрабатываем все исключения
        return str(e)  
    finally:
        ssh.close()


# Получаем список серверов из переменной окружения
servers_str = os.getenv('Servers')

# Преобразуем строку в список
servers = servers_str.split(', ')

os_types = []
for server in servers:
    os_type = try_to_connect(server)
    os_types.append(os_type)
        
print(os_type)
