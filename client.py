import socket
import threading
import os
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
    # THREAD DE RECEBIMENTO
    # ============================
    
    def receber_mensagens():
        while True:
            try:
                # Fica aguardando a resposta do servidor
                response = client.recv(1024).decode()
                
                # Se a resposta for vazia ou 'exit', encerra
                if not response or response.lower() in ['exit']:
                    print("\n[Aviso] O servidor encerrou o chat.")
                    client.close()
                    os._exit(0) # Força o encerramento do programa
                    
                # Captura a hora e exibe a mensagem recebida
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print(f"\r\033[K[{hora_atual}] Servidor: {response}")
                
                # Reescreve o prompt para o usuário não se perder
                print("Digite sua mensagem: ", end="", flush=True)
                
            except ConnectionAbortedError:
                break
            except ConnectionResetError:
                print("\n[Erro] O servidor foi desconectado bruscamente.")
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
        # Cliente digita a mensagem
        message = input("Digite sua mensagem: ")
        
        hora_atual = datetime.now().strftime("%H:%M:%S")
        
        # Apaga a linha do input e imprime o formato definitivo
        print(f"\033[A\033[K[{hora_atual}] Você: {message}")
        
        # Envia a mensagem
        client.send(message.encode())
        
        if message.lower() in ['exit']:
            print("\nVocê encerrou o chat.")
            break

except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor. Verifique se ele está rodando.")

finally:
    
    # ============================
    # ENCERRAMENTO
    # ============================
    client.close()
    print("Cliente encerrado.")
