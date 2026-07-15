import socket

# ============================
# CONFIGURAÇÕES DO SERVIDOR
# ============================

HOST = "127.0.0.1"      # Endereço local (localhost)
PORT = 5000             # Porta escolhida

# ============================
# CRIAÇÃO DO SOCKET
# ============================

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao IP e à porta
server.bind((HOST, PORT))

# Coloca o servidor em modo de espera
server.listen(1)

print("=" * 40)
print("SERVIDOR TCP")
print("=" * 40)
print(f"Servidor iniciado em {HOST}:{PORT}")
print("Aguardando conexão do cliente...")
print("=" * 40)

# Aguarda até que um cliente se conecte
client_socket, client_address = server.accept()

print(f"Cliente conectado: {client_address}")
print("Conexão estabelecida com sucesso!")

# Fecha a conexão do cliente
client_socket.close()

# Fecha o servidor
server.close()

print("Servidor encerrado.")