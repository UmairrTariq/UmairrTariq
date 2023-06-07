# - building a weather application in Python using the OpenWeatherMap API
import requests
import json

def get_weather(city):

    api_key= '4644a7f2ffb88a4820b1030e0a112417'
    base_url= 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q' : city,
        'appid' : api_key,
        'units' : 'metric'
    }

    response = requests.get(base_url,params=params)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        print('City not Found, Please Check the Spelling.')

    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']


    print(f'Weather in {city}: ')
    print(f'Temperature : {temp} °C')
    print(f'Humidity : {humidity}%')
    print(f'Description : {description}')

city = 'Karachi'
get_weather(city)