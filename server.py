import socket

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

print("=" * 40)
print("SERVIDOR TCP")
print("=" * 40)
print(f"Servidor iniciado em {HOST}:{PORT}")
print("Aguardando conexão do cliente...")
print("=" * 40)

# Aguarda conexão
client_socket, client_address = server.accept()

print(f"Cliente conectado: {client_address}")
print("Conexão estabelecida com sucesso!")

# ============================
# RECEBE MENSAGEM DO CLIENTE
# ============================

message = client_socket.recv(1024).decode()

print(f"Cliente: {message}")

# ============================
# ENVIA RESPOSTA
# ============================

response = "Olá! Tudo bem?"

client_socket.send(response.encode())

print("Resposta enviada!")

client_socket.close()
server.close()

print("Servidor encerrado.")