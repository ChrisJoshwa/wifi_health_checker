def parse_output(ssh_client, command):
    try:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode().strip()
        return output if output else None
    except Exception:
        return None

