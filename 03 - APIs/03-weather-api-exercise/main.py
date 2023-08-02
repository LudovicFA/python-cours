import requests

def get_weather(lat, lon, api_key='e248997c5de859f6e9d8c4c131a505f2'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
    print(url)
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file: 
        for dict in content['list']:
            file.write(f"Nantes,{dict['main']['temp']},{dict['weather'][0]['description']}\n")
    return content
    
print(get_weather(lat='48.862725', lon='2.287592'))