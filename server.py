import socket
from datetime import datetime

# ============================
# CONFIGURAÇÕES DO SERVIDOR
# ============================

HOST = "127.0.0.1"
PORT = 5000

# ============================
# CRIAÇÃO DO SOCKET
# ============================

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("=" * 50)
print("SERVIDOR TCP")
print("=" * 50)
print(f"Aguardando conexão em {HOST}:{PORT}...")

# Aguarda conexão
client_socket, client_address = server.accept()
print(f"Cliente conectado: {client_address}")
print("Chat iniciado! (Digite 'exit' para encerrar)")
print("=" * 50)


# ============================
# LOOP DE COMUNICAÇÃO
# ============================

while True:
    
    print("Aguardando resposta...")
    
    message = client_socket.recv(1024).decode()
    
    print("\033[A\033[K", end="") #Apaga a mensagem "Aguardando resposta..."

    if not message or message.lower() in ['exit']:
        print("\nO cliente encerrou o chat.")
        break
    
    hora_atual = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora_atual}] Cliente: {message}")
    
    response = input("Digite sua mensagem: ")
    
    hora_atual = datetime.now().strftime("%H:%M:%S")
    
    print(f"\033[A\033[K[{hora_atual}] Você: {response}") #Apaga a mensagem "Digite sua mensagem" e substitui por "Você:"
    
    client_socket.send(response.encode())
    
    if response.lower() in ['sair', 'exit']:
        print("\nVocê encerrou o chat.")
        break

# ============================
# ENCERRAMENTO
# ============================

client_socket.close()
server.close()
print("Servidor encerrado.")
