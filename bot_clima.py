import requests
import

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1512146194187419799/dUGIsAVqbGf_dPnJj0tkyzhdynzpgCY-v-I7PUdLO1ZsAIjIB_eDVepvGqu7VdnTAOww"
API_CLIMA_URL = "https://api.hgbrasil.com/weather?key=development&city_name=Ananindeua,PA"

def verificar_clima()
     try:
        requisicao - requests.get(API_CLIMA_URL)
        dados = requisicao.json()

        resultados = dados["results"]
        temperatura = resultados["temp"]
        descricao = resultados["description"]
        cidade = resultados["city"]
        chuva = resultados["ccondition_slug"] 

        print(f"Tempo esta assim ma {cidade}: {temperatura}°C e {descricao}")

        if chuva in ["rain", "strom"]:
            payload = {
                "content": f" CHUVA EM ANANINDEUA. TEMPO ESTÁ MARCANDO {temperatura}°C com {descricao}. Cuidado!"
            }

            requests.post(WEBHOOK_URL, json=payload)
            print("alerta de chuva enviado para discord")

            else:
                payload = {
                    "content": f" relatório tempo {temperatura} agora esta fazendo {temperatura}°C com {descricao}"
                }
                requests.post(WEBHOOK_URL, json=payload)
                print("relatório diário enviado para o discord")

            except excption as e:
                print(f"ocorreu um erro ao processar os dados: {e}")

                verificar_clima()

