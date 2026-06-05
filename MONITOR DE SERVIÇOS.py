import requests
import time
import psutil

WEBHOOK_URL = "python-dotenv"

IntegraWebService = "srvIntegraWeb"

def verificar_serico_windows():
    try:
        servico = psutil.win_service_get(IntegraWebService)
        status_atual = servico.status()

        print(f"Status atual do servico [{IntegraWebService}]: {status_atual}")

        if status_atual == "stopped":
            print(f"ALERTA O SERVICO {IntegraWebService} PAROU")

            payload = {
                "content": f"🚨 ALERTA CRITICO O SERVICO {IntegraWebService} PAROU "
            }
            requests.post(WEBHOOK_URL, json=payload)

        
            try:
                servico.start()
                print("tentativa de reinicializacao enviado")
                time.sleep(5)

                if servico.status() == "running":
                    payload_sucesso = {
                        "content": f" 🥳 RECUPERADO. O SERVICO {IntegraWebService} VOLTOU"
                    }
                    requests.post(WEBHOOK_URL, json=payload_sucesso)
            except Exception as erro_start:
                print(f"NAO FOI POSSIVEL INICIAR O SERVICO: {erro_start}")

    except Exception as e:
        print(f"Erro geral no monitoramento: {e}")


while True:
    verificar_serico_windows()
    time.sleep(10)