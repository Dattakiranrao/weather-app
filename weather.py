import requests

API_KEY = 'Enter your api which can be generated on site'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')

request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    name = data['name']
    print(name)
    weather = data['weather'][0]['description']
    print(weather)
    temperature = data['main']['temp'] - 273.15
    print(f"{round(temperature, 2)}`C")
    country = data['sys']['country']
    print(country)
else:
    print("an error occurred.")

