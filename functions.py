import requests, json, datetime 

# Dont change anything here, head over to config.json if you wish to manually write your keys there
configuration = {
  "weatherKey": "00000000000000000000000000000000", 
  "DiscordWebHook": ""
}

# Does what it says, returns current configured keys
def getKeys():
    f = open("config.json", "r")
    f = json.load(f)
    weatherKey = f["weatherKey"]
    DiscordWebHook = f["DiscordWebHook"]
    return weatherKey, DiscordWebHook

# Function allowing user to change/add his OpenWeatherMap API key or Discord webhook url trough a terminal
def changeConfig(weatherKey = "", webhookUrl = ""):
    configuration["weatherKey"] = weatherKey
    configuration["DiscordWebHook"] = webhookUrl
    f = open("config.json", "w")
    json.dump(configuration, f)

# Function returning status codes for both connections, debbuging
def testConnection():
    results = {}
    weatherKey, DiscordWebHook = getKeys()
    url = f'https://api.openweathermap.org/data/2.5/weather?q=New York&appid={weatherKey}'
    try:
        r = requests.get(url)
        results["WeatherAPI"] = r.status_code
    except Exception:
        results["WeatherAPI"] = -1
    try:
        r = requests.get(DiscordWebHook)
        results["DiscordWebhook"] = r.status_code
    except Exception:
        results["DiscordWebhook"] = -1
    return results

# Returns a dictionary with data received from OpenWeatherMap
def requestWeatherData(weatherKey, city):
    t = testConnection()
    if t["WeatherAPI"] != 200:
        print(f"Invalid connection! Error code: {t["WeatherAPI"]}")
        return
    else:    
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherKey}"
        try:
            r = requests.get(url)
            WeatherData = r.json()
            data = {}
            data["Location"] = WeatherData["name"]
            data["Country"] = WeatherData["sys"]["country"]
            data["Longitude / Latitude"] = f"{WeatherData['coord']['lon']} / {WeatherData['coord']['lat']}"
            data["Weather"] = WeatherData["weather"][0]["main"]
            data["Description"] = WeatherData["weather"][0]["description"]
            data["Temperature"] = round(WeatherData["main"]["feels_like"] - 273.15, 2)
            data["Humidity"] = WeatherData["main"]["humidity"]
            data["Pressure"] = WeatherData["main"]["pressure"]
        except Exception:
            print("Can't retrieve information about that city!")
            return
    return data

# Converts data into a readable format for the user, sends the same data to discord webhook
def sendData(data, discord):
    message = ""
    for key, value in data.items():
                print(f"{key}: {value}")
                message += f"{key}: {value}\n"
    try:
        requests.post(discord, json={"content": message})
    except Exception:
        print("Couldn't send information to discord. ")    
    