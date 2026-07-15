import socket

# ============================
# CONFIGURAÇÕES DO CLIENTE
# ============================

SERVER_IP = "127.0.0.1"      # Endereço do servidor (localhost)
SERVER_PORT = 5000           # Mesma porta definida no servidor

# ============================
# CRIAÇÃO DO SOCKET
# ============================

# Cria o socket do cliente (AF_INET = IPv4, SOCK_STREAM = TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("=" * 40)
print("CLIENTE TCP")
print("=" * 40)
print(f"Tentando conectar ao servidor em {SERVER_IP}:{SERVER_PORT}...")

try:
    # Conecta ao servidor
    client.connect((SERVER_IP, SERVER_PORT))
    print("Conectado ao servidor!")
    
except ConnectionRefusedError:
    print("Erro: Não foi possível conectar. Verifique se o servidor está rodando.")

finally:
    # Fecha a conexão do cliente
    client.close()
    print("Cliente encerrado.")
    print("=" * 40)
