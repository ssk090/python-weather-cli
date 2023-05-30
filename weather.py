import requests
import json
import os
import argparse


def get_weather(city):
    """Gets the current weather forecast for a city."""

    # Get the API key from the environment variable.
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    if api_key is None:
        raise Exception("OpenWeatherMap API key not found.")

    # Make the API request.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    # Check the response status code.
    if response.status_code != 200:
        raise Exception(f"Error getting weather forecast: {response.status_code}")

    # Parse the JSON response.
    weather_data = json.loads(response.content)

    return weather_data


def get_emoji(weather_id):
    """Gets the corresponding emoji for a weather condition."""

    # Map weather conditions to emojis.
    emoji_map = {
        200: "thunderstorm with light rain ⛈️",
        201: "thunderstorm with rain ⛈️",
        202: "thunderstorm with heavy rain ⛈️",
        210: "light thunderstorm ⛈️",
        211: "thunderstorm ⛈️",
        212: "heavy thunderstorm ⛈️",
        221: "ragged thunderstorm ⛈️",
        230: "thunderstorm with light drizzle ⛈️",
        231: "thunderstorm with drizzle ⛈️",
        232: "thunderstorm with heavy drizzle ⛈️",
        300: "light intensity drizzle 🌧️",
        301: "drizzle 🌧️",
        302: "heavy intensity drizzle 🌧️",
        310: "light intensity drizzle rain 🌧️",
        311: "drizzle rain 🌧️",
        312: "heavy intensity drizzle rain 🌧️",
        313: "shower rain and drizzle 🌧️",
        314: "heavy shower rain and drizzle 🌧️",
        321: "shower drizzle 🌧️",
        500: "light rain 🌧️",
        501: "moderate rain 🌧️",
        502: "heavy intensity rain 🌧️",
        503: "very heavy rain 🌧️",
        504: "extreme rain 🌧️",
        511: "freezing rain 🌧️",
        520: "light intensity shower rain 🌧️",
        521: "shower rain 🌧️",
        522: "heavy intensity shower rain 🌧️",
        531: "ragged shower rain 🌧️",
        600: "light snow ❄️",
        601: "snow ❄️",
        602: "heavy snow ❄️",
        611: "sleet ❄️",
        612: "light shower sleet ❄️",
        613: "shower sleet ❄️",
        615: "light rain and snow ❄️",
        616: "rain and snow ❄️",
        620: "light shower snow ❄️",
        621: "shower snow ❄️",
        622: "heavy shower snow ❄️",
        701: "mist ☁️",
        711: "smoke ☁️",
        721: "haze ☁️",
        731: "dust ☁️",
        741: "fog ☁️",
        751: "sand ☁️",
        761: "dust ☁️",
        762: "volcanic ash ☁️",
        771: "squalls ⚠️",
        781: "tornado ⚠️",
        800: "clear sky ☀️",
        801: "few clouds ☀️",
        802: "scattered clouds ☀️",
        803: "broken clouds ☀️",
        804: "overcast clouds ☀️",
    }

    # Return the corresponding emoji.
    return emoji_map.get(weather_id, "❓")


def main():
    """Gets the current weather forecast for a city or location."""

    print(
        """

██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗    ██████╗ ██╗   ██╗
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝   ██████╔╝ ╚████╔╝ 
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗   ██╔═══╝   ╚██╔╝  
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║██╗██║        ██║   
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                                                               

    """
    )
    # Create the parser.
    parser = argparse.ArgumentParser(description="Get the current weather forecast.")

    # Add the location argument.
    parser.add_argument(
        "-l", "--location", help="The location to get the weather forecast for."
    )

    # Parse the arguments.
    args = parser.parse_args()

    # Get the weather forecast.
    weather_data = get_weather(args.location)

    # Get the weather condition.
    weather_condition = weather_data["weather"][0]["description"]
    weather_id = weather_data["weather"][0]["id"]

    # Get the temperature.
    temperature = weather_data["main"]["temp"]

    # Convert temperature from Kelvin to Celsius.
    temperature_celsius = temperature - 273.15

    # Get the corresponding emoji.
    emoji = get_emoji(weather_id)

    # Print the weather forecast with emojis.
    print(f"{args.location} : {emoji} " f"  temp : {temperature_celsius:.2f}°C")


if __name__ == "__main__":
    main()
