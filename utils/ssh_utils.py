import paramiko

def ssh_connect(ip, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, timeout=5)
        return client
    except Exception as e:
        print(f"Connection to {ip} failed: {e}")
        return None

