# README - Script de envío de pronóstico del clima con temperaturas menores a 10 grados

Este es un script de Python que utiliza la biblioteca Pandas, solicita datos a una API de pronóstico del clima y envía un mensaje de texto con el pronóstico del tiempo para una ciudad específica, incluyendo las horas en las que la temperatura es inferior a 10 grados Celsius.

## Requisitos
- Python 3.x
- Instalar las siguientes bibliotecas:
    - pandas
    - requests
    - tqdm
    - twilio

## Configuración
Antes de ejecutar el script, asegúrate de configurar los siguientes parámetros en el archivo `twilio_config.py`:
- `TWILIO_ACCOUNT_SID`: SID de tu cuenta de Twilio.
- `TWILIO_AUTH_TOKEN`: Token de autenticación de Twilio.
- `PHONE_NUMBER`: Número de teléfono Twilio desde el cual se enviará el mensaje.
- `API_KEY_WAPI`: Clave de API de WeatherAPI.
- `PHONE_NUMBER_2`: Número de teléfono al cual se enviará el mensaje.

## Uso
1. Ejecuta el script `msj_twilio.py` desde la línea de comandos o desde tu entorno de desarrollo preferido.
2. El script obtendrá los datos del pronóstico del clima para la ciudad especificada en la variable `query` mediante la API de WeatherAPI.
3. A continuación, se realizarán algunas transformaciones en los datos y se creará un DataFrame de Pandas que contiene las horas, las condiciones climáticas y las temperaturas para las horas con temperaturas inferiores a 10 grados Celsius entre las 6 AM y las 10 PM.
4. El script enviará un mensaje de texto a través de Twilio con el pronóstico del tiempo para la ciudad y las horas con temperaturas menores a 10 grados Celsius.

Ten en cuenta que es necesario tener una cuenta de Twilio y configurar los parámetros correctamente para poder enviar mensajes de texto.

**Nota:** Asegúrate de que el número de teléfono especificado en `PHONE_NUMBER_2` sea válido y esté registrado en Twilio para recibir el mensaje correctamente.

## Créditos
Autor: Jorge
Versión: 4.0

Este script fue desarrollado por Jorge como parte de un ejercicio de programación. Puedes contactar a Jorge en jorgeflores2311233@gmail.com para cualquier pregunta o sugerencia relacionada con el script.

## Licencia
Este script se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para obtener más información.
