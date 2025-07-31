# WeatherBot
A simple Python app for checking the weather, with Discord webhook integration.
Every time you request to see informatio about a city, it also sends information to the discord webhook. 
# Capabilities
The app uses OpenWeatherMap API to fetch current weather data for any city. The data is displayed in the terminal and also sent to a Discord webhook of your choice. It contains a simple JSON-based config file for persistent settings
You are able to test your connection, request data as well as configure your config file directly from the app. 
# How to use
- Create an account on [OpenWeatherMap](https://openweathermap.org/)
- Generate an [API key](https://home.openweathermap.org/api_keys)
- Run the setup function in the app, put your API key in there and discord webhook, if you have one
- Run the test function and make sure everything is working, you are good to go!
# Planned features
- Automatic scheduling, send updates to Discord webhook in a scheduled user-defined intervals
- Weather forecast and alerts for severe weather conditions
- ~Error handling~
- ~Discord responses in pretty embeds~
  
