import os
import paramiko
 
# Получение имени пользователя и пароля из переменных окружения
username = os.getenv('ansible_user')
password = os.getenv('ansible_pass')
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
try:
    ssh.connect('stg-rl-k8s-n05.digi.loc', username=username, password=password)
    print("Connected successfully")
except paramiko.AuthenticationException:
    print("Failed to connect")
finally:
    ssh.close()