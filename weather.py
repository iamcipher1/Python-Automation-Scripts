import requests
from datetime import datetime

API_KEY = '35a2115467ae447e97f115614252611'

def get_weather(city):
  
    
    url =f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    try:
      response= requests.get(url, timeout =10)
      response.raise_for_status()
    except requests.exceptions.RequestException as e:
      return f'Error: Could not connect \n Details:{e}'
    today= datetime.now().strftime('%d-%m-%Y')
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data =response.json()
    location = data['location']['name']
    region= data['location']['region']
    country= data['location']['country']
    local_time=data['location']['localtime']
    temp_c= data['current']['temp_c']
    feels_c= data['current']['feelslike_c']
    condition= data['current']['condition']['text']
    try:
      with open('weather_log.txt','r')as f:
        if today in f.read():    
          return('Today\'s weather already logged') 
          
    except FileNotFoundError:
      pass    

    
    with open ('weather_log.txt','w') as f:
      f.write(f'''=== Weather log {timestamp}===: City: {location},Country:{country}:
           Localtime:{local_time}
           Temperature: {temp_c}°C
           Feel like: {feels_c}°C
           Condition: {condition}\n''')
    return 'Weather logged successfully'
city='Abuja'
print (get_weather(city))
