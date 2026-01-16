import socket
from datetime import datetime
import os 



def settup_logs():
    if not os.path.exists("logs"):
        os.mkdir("logs")
        print("Directorio de logs creado")
        print("No existian las carpetas de logs")


def is_valid_IP(ip):
    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        number = int(part)
        
        if number < 0 or number > 255:
            return False
    return True




#Funcion del port scanner
def scan(ip, port, timeout=0.6):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    
    try:
        s.connect((ip, port))
        s.close()
        return "Open"
    except socket.timeout:
        s.close()
        return "Filtered"
    except ConnectionRefusedError:
        s.close()
        return "Closed"
    except Exception:
        s.close()
        return "Error"
        
    

#Se crea la funcion del logger 
def logger(ip,port,state):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} - {ip} - {port} - {state}\n"
    
    with open("logs/scan_log.txt", "a") as f:
        f.write(line)

#Funcion principal
def main():
    print("----Bienvenido al port scanner de R0T0M----")
    print("----Creado por R0T0M----")
    print("----Version 1.0----")
    print("----Escanee puertos TCP y registre sus resultados----")
    while True:
        ip = input("IP a escanear (o exit para salir): ").strip()
        if ip.lower() == "exit":
            print("Saliendo del programa...")
            break
        if not is_valid_IP(ip):
            print("La direccion IP no es valida. Formato: XXX.XXX.XXX.XXX o IPv4")
            continue
    
        try:
            max_port = int(input("Escanear puertos desde 1 hasta: "))
            if max_port <= 0 or max_port > 65535:
                raise ValueError
        except ValueError:
            print("Puerto inválido. Debe estar entre 1 y 65535.")
            continue
        
        print("Escaneando...")
        for port in range(1, max_port + 1):
            state = scan(ip, port)
            print(f"Port {port}: {state}")
            logger(ip,port,state)
            
            
        print("Escaneo completo. Resultados guardados en log.txt")
    
if __name__ == "__main__":
    main()
    