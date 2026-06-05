import requests
import time

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1512146194187419799/dUGIsAVqbGf_dPnJj0tkyzhdynzpgCY-v-I7PUdLO1ZsAIjIB_eDVepvGqu7VdnTAOww"
API_FUTEBOL_URL = "https://dashboard.api-football.com/soccer/tester"

def verificar_placar():
      try:
        requisicao = requests.get(API_FUTEBOL_URL)
        dados = requisicao.json()

        status_jogo = str(dados.get("status", "Em Andamento"))

        print(f"Status atual do jogo: {status_jogo}")

        ALVO ="Penalty"

        if status_jogo < ALVO:
            payload = {
                "content": f"🚨 **ALERTA HOUVE PENALTI! {status_jogo} FIQUE DE OLHO"
            }

            requests.post(WEBHOOK_URL, json=payload)
            print(f"ALERTA ENVIADO PARA O DISCORD!")

except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")

        while true:
            verificar_placar()
            time.sleep(30)
