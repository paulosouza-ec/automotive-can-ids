import can
import time

# --- Parâmetros do Ataque de Diagnóstico ---

# Nome da interface CAN na Raspberry Pi.
CAN_INTERFACE = 'can0'

# ID padrão para requisições de diagnóstico (OBD-II).
DIAGNOSTIC_REQUEST_ID = 0x7DF

# Payload para solicitar a Rotação do Motor (RPM).
RPM_REQUEST_PAYLOAD = [0x02, 0x01, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00]

# --- MUDANÇAS AQUI ---
# Duração total do ataque em segundos.
ATTACK_DURATION_SECONDS = 30

# Intervalo entre cada requisição (em segundos).
REQUEST_INTERVAL_SECONDS = 0.2

# --- Lógica do Ataque ---

def run_diagnostic_attack_timed():
    """
    Executa um ataque de diagnóstico enviando requisições OBD-II
    periodicamente por um tempo determinado.
    """
    print("Iniciando o Ataque de Diagnóstico (versão por tempo)...")
    print(f"Enviando requisições para RPM por {ATTACK_DURATION_SECONDS} segundos.")
    
    bus = None
    try:
        bus = can.interface.Bus(channel=CAN_INTERFACE, bustype='socketcan')

        msg = can.Message(
            arbitration_id=DIAGNOSTIC_REQUEST_ID,
            data=RPM_REQUEST_PAYLOAD,
            is_extended_id=False
        )

        start_time = time.time()
        message_count = 0

        # --- ESTRUTURA DO LOOP MODIFICADA ---
        # Loop que roda por um tempo determinado em vez de um número fixo de vezes.
        while time.time() - start_time < ATTACK_DURATION_SECONDS:
            bus.send(msg)
            message_count += 1
            print(f"  Requisição enviada. Contagem: {message_count}", end='\r')
            time.sleep(REQUEST_INTERVAL_SECONDS)

        end_time = time.time()

        print(f"\n\n--- Ataque de Diagnóstico Finalizado ---")
        print(f"Duração total: {end_time - start_time:.2f} segundos.")
        print(f"Total de requisições enviadas: {message_count}")

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

    finally:
        if bus:
            bus.shutdown()
            print("Conexão com o barramento CAN foi encerrada.")


if __name__ == "__main__":
    run_diagnostic_attack_timed()