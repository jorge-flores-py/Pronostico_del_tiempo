import pandas as pd 
import requests
import time 
from tqdm import tqdm
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI,PHONE_NUMBER_2

# Python Inicial [Python]
# Ejercicio de envio de pronostico del clima con temperaturas menores a 10 grados

# Autor: Jorge
# Version: 4.0

#creamos una funcion que tome los datos y no de los que vamos a enviar  en el mensaje 
def get_info(data,i):
    fecha = data['forecast']['forecastday'][0]['hour'][i]['time'].split()[0] # Fecha
    hora = int(data['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0]) # Hora
    condicion = data['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    temperatura = data['forecast']['forecastday'][0]['hour'][i]['temp_c']
    llovera =  data['forecast']['forecastday'][0]['hour'][i]['will_it_rain'] # 1 llovera o no llovera
    prob_lluvia = data['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
   
    return fecha, hora, condicion, temperatura, llovera, prob_lluvia

if __name__ == "__main__":
    #Obtenemos datos de la API
    print("Obteniendo datos de la API")
    query = 'Buenos Aires'  # Eleguimos la ciudad donde queremos buscar el pronostico
    apy_key = API_KEY_WAPI
    url_clima = f'http://api.weatherapi.com/v1/forecast.json?key={apy_key}&q={query}&days=1&aqi=no&alerts=no'
    response = requests.get(url_clima)
    data= response.json()
    
    #Inicializamos variables
    datos = []
    cantidad =len(data['forecast']['forecastday'][0]['hour'])

    for i in tqdm(range(cantidad),colour='red'):
        datos.append(get_info(data,i))
    
    # Realizamos las transformaciones y creamos el df
    columnas = ['fecha', 'hora', 'condicion', 'temperatura', 'llovera', 'prob_lluvia']
    df = pd.DataFrame(datos,columns=columnas)
    df_temp_menor_10grados =df[(df['temperatura']<10) & (df['hora']>6) & (df['hora']<22)]
    df_temp_menor_10grados = df_temp_menor_10grados[['hora','condicion','temperatura']]
    df_temp_menor_10grados.set_index('hora', inplace=True)
    
    # Envio de msj
    time.sleep(2)
    account_sid = TWILIO_ACCOUNT_SID 
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body='\nHola! \n\n\n El pronostico del tiempo hoy con las horas por debajo de los 10°c '+ df['fecha'][0] +' en ' + query +' es : \n\n\n ' + str(df_temp_menor_10grados),
                        from_= PHONE_NUMBER ,
                        to= PHONE_NUMBER_2
                    )
    print('Mensaje Enviado ' + message.sid)