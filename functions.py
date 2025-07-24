import requests, json

# Dont change anything here, head over to config.json if you wish to manually write your keys there
configuration = {
  "weatherKey": "00000000000000000000000000000000", 
  "DiscordWebHook": ""
}

# Does what it says, returns current configured keys
def getKeys():
    f = json.load(open("config.json", "r"))
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
    r = requests.get(weatherKey)
    results["WeatherAPI"] = r.status_code
    r = requests.get(DiscordWebHook)
    results["DiscordWebhook"] = r.status_code
    return results

# Returns a dictionary with data received from OpenWeatherMap
def requestWeatherData(weatherKey):
    r = requests.get(weatherKey)
    WeatherData = r.json()
    return WeatherData