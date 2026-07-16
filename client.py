import socket
from datetime import datetime

# ============================
# CONFIGURAÇÕES DO CLIENTE
# ============================

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

# ============================
# CRIAÇÃO DO SOCKET
# ============================

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("=" * 50)
print("CLIENTE TCP")
print("=" * 50)

try:
    client.connect((SERVER_IP, SERVER_PORT))
    print("Conectado ao servidor! (Digite 'exit' para encerrar)")
    print("=" * 50)


# ============================
# LOOP DE COMUNICAÇÃO
# ============================
    
    while True:

        message = input("Digite sua mensagem: ")
        hora_atual = datetime.now().strftime("%H:%M:%S")
        
        print(f"\033[A\033[K[{hora_atual}] Você: {message}") #Apaga a mensagem "Digite sua mensagem" e substitui por "Você:"
        
        client.send(message.encode())
        
        if message.lower() in ['exit']:
            print("\nVocê encerrou o chat.")
            break

        print("Aguardando resposta...")

        response = client.recv(1024).decode()
        
        print("\033[A\033[K", end="") #Apaga a mensagem "Aguardando resposta..."
        
        if not response or response.lower() in ['sair', 'exit']:
            print("\nO servidor encerrou o chat.")
            break
            
        hora_atual = datetime.now().strftime("%H:%M:%S")
        print(f"[{hora_atual}] Servidor: {response}")

except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor.")

finally:

# ============================
# ENCERRAMENTO
# ============================

    client.close()
    print("Cliente encerrado.")
    print("=" * 50)
