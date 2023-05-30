# weather-python-cli tool
- The is a Python program that gets the current weather forecast for a city or location. 
- The program first prints a header with some ASCII art. Then, it creates an ArgumentParser object to parse the command-line arguments. 
- The only required argument is the location to get the weather forecast for. 
- The program then calls the get_weather() function to get the weather forecast for the specified location. 
- The get_weather() function makes an API request to the OpenWeatherMap API. 
- The API response is a JSON object. The get_weather() function parses the JSON object and returns a dictionary containing the weather forecast data. 
- The program then gets the weather condition, temperature, and emoji for the specified location. 
- The program then prints the weather forecast with emojis.

<img width="627" alt="image" src="https://github.com/ssk090/python-weather-cli/assets/22127725/3dac8efd-b315-4c2d-a002-a833562721d9">


## Key Features
- The code uses the OpenWeatherMap API to get the weather forecast.
- The code parses the JSON response from the OpenWeatherMap API.
- The code prints the weather forecast with emojis.
