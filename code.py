#Функция для удаления с сервера Linux
import platform
import subprocess

def remove_zabbix_agent():
    # Получаем информацию о типе операционной системы
    os_type = platform.system()

    if os_type == "Linux":
        # Команды для удаления Zabbix Agent на разных типах Linux

        # Ubuntu/Debian
        if "ubuntu" in platform.linux_distribution()[0].lower() or "debian" in platform.linux_distribution()[0].lower():
            command = "sudo apt-get remove zabbix-agent"

        # CentOS/RHEL
        elif "centos" in platform.linux_distribution()[0].lower() or "redhat" in platform.linux_distribution()[0].lower():
            command = "sudo yum remove zabbix-agent"

        # Другие дистрибутивы Linux
        else:
            print("Данный дистрибутив Linux не поддерживается.")
            return

        # Выполняем команду для удаления Zabbix Agent
        try:
            subprocess.run(command, shell=True, check=True)
            print("Zabbix Agent успешно удален.")
        except subprocess.CalledProcessError as e:
            print("Ошибка при удалении Zabbix Agent:", e)
    else:
        print("Данная функция поддерживается только на Linux-серверах.")
        
