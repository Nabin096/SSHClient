import paramiko

hostname = 'xx.xx.xx.xx'
port = 22
username = 'cccyyy'
password = 'xxxxxyyyy'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    #print(stdout.read())
    #app.run(host='0.0.0.0', port=80)
    s.close()
