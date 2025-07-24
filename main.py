import requests, functions, json
decision = input('Welcome to weather app!\nWhat would you like to do?:\n1. "s" for setup/configuration\n2. "d" to request data\n3. "t" to test the connection\n4. "q" to exit\n')
while decision != "q":
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
            functions.sendData(data, discord)
        case "t":
            results = functions.testConnection()
            for type, status in results.items():
                print(f"{type}: {status}") 
        case "q":
            exit()
    decision = input('s - setup, d - request data, t - test connection, q - quit: ')