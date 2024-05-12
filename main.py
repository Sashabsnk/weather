import requests
while True:
    api_key = "66b9ff3604c5ccaf931042abbaef1abf"
    city = input("ведите название города ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data['weather'][0]['description']
        temp = data ['main']["temp"]
        print(f"погода в городе {city}: {weather}, temp: {temp}℃")
    else:
        print('город не найден')
