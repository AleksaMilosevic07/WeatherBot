import requests, functions, json
decision = input('Welcome to weather app!\nWhat would you like to do?:\n1. "s" for setup/configuration\n2. "d" to request data\n3. "q" to exit\n')
while decision != "q":
    decision = input('s - setup, d - request data, q - quit: ')
    match decision:
        case "s": 
            w = input("Your OpenWeatherMap API key: ")
            d = input("Your Discord web hook url: ")
            functions.changeConfig(w, d)
        case "d":
            f = open("config.json", "r")
            f = json.load(f)
            key, discord = f["weatherKey"], f["DiscordWebHook"]
            city = input("Which city would you like to view?: ")
            data = functions.requestWeatherData(key, city)
            print(data)
            requests.post(discord, data)
        case "q":
            exit()