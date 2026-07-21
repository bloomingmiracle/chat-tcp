import socket
import threading
import os
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
# THREAD DE RECEBIMENTO
# ============================

def receber_mensagens():
    while True:
        try:
            # Fica aguardando a mensagem do cliente
            message = client_socket.recv(1024).decode()
            
            # Se a mensagem for vazia ou 'exit', encerra
            if not message or message.lower() in ['exit']:
                print("\n[Aviso] O cliente encerrou o chat.")
                client_socket.close()
                server.close()
                os._exit(0) # Força o encerramento do programa
                
            hora_atual = datetime.now().strftime("%H:%M:%S") # Captura a hora e exibe a mensagem recebida

            print(f"\r\033[K[{hora_atual}] Cliente: {message}") # \r volta ao início da linha, \033[K apaga a linha atual
            
            # Reescreve o prompt para o usuário não se perder
            print("Digite sua mensagem: ", end="", flush=True)
            
        except ConnectionResetError:
            print("\n[Erro] Conexão perdida com o cliente.")
            os._exit(0)
        except Exception:
            break

# Inicia a função receber_mensagens() rodando em paralelo
thread = threading.Thread(target=receber_mensagens, daemon=True)
thread.start()

# ============================
# LOOP DE ENVIO (FLUXO PRINCIPAL)
# ============================

while True:
    try:
        # Servidor digita a resposta
        response = input("Digite sua mensagem: ")
        
        hora_atual = datetime.now().strftime("%H:%M:%S")
                
        print(f"\033[A\033[K[{hora_atual}] Você: {response}") # Apaga a linha do input e imprime o formato definitivo
        
        client_socket.send(response.encode())
        
        if response.lower() in ['exit']:
            print("\nVocê encerrou o chat.")
            break
            
    except Exception:
        break

# ============================
# ENCERRAMENTO
# ============================
client_socket.close()
server.close()
print("Servidor encerrado.")
