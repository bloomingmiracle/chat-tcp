import socket

# ============================
# CONFIGURAÇÕES DO CLIENTE
# ============================

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

# ============================
# CRIAÇÃO DO SOCKET
# ============================

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("=" * 40)
print("CLIENTE TCP")
print("=" * 40)
print(f"Tentando conectar ao servidor em {SERVER_IP}:{SERVER_PORT}...")

try:

    client.connect((SERVER_IP, SERVER_PORT))

    print("Conectado ao servidor!")

    # ============================
    # ENVIA MENSAGEM
    # ============================

    message = "Olá!"

    client.send(message.encode())

    print(f"Mensagem enviada: {message}")

    # ============================
    # RECEBE RESPOSTA
    # ============================

    response = client.recv(1024).decode()

    print(f"Servidor: {response}")

except ConnectionRefusedError:

    print("Erro: Não foi possível conectar.")

finally:

    client.close()

    print("Cliente encerrado.")
    print("=" * 40)