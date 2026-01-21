import requests

def get_weather(city: str, api_key: str):
    """
    Fetches the current temperature for a given city.
    Requires a valid OpenWeatherMap API key.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    print(f"--- Fetching Weather for {city} ---")
    
    try:
        response = requests.get(url, params=params, timeout=5)
        
        # raise_for_status() will throw an exception for 4xx or 5xx codes
        response.raise_for_status()
        
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        
        print(f"In {city}, it is currently {temp}°C with {desc}.")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Note: This will fail until a valid API key is provided
    MY_API_KEY = "YOUR_API_KEY_HERE" 
    get_weather("Wels,AT", MY_API_KEY)
