import requests

class ExternalServices:
    def __init__(self):
        self.api_key = "your_api_key_here"  # Replace with your actual API key
        self.weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    def get_weather(self, city):
        """
        Fetches the weather data for a specified city using the OpenWeatherMap API.
        """
        complete_url = f"{self.weather_base_url}appid={self.api_key}&q={city}"
        try:
            response = requests.get(complete_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            data = response.json()
            
            if data["cod"] != "404":
                main = data["main"]
                weather_desc = data["weather"][0]["description"]
                temperature = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]

                weather_report = (
                    f"Weather in {city}:\n"
                    f"Temperature: {temperature - 273.15:.2f}°C\n"
                    f"Atmospheric pressure: {pressure} hPa\n"
                    f"Humidity: {humidity}%\n"
                    f"Description: {weather_desc.capitalize()}"
                )
                print(weather_report)
                return weather_report
            else:
                print("City not found.")
                return "City not found."

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch weather data: {e}")
            return None
    
    def get_data_from_api(self, url, params=None):
        """
        Generic method to fetch data from any external API.
        """
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            data = response.json()
            print(f"Data fetched successfully from {url}")
            return data

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data from {url}: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    services = ExternalServices()

    # Example: Get weather data
    weather_report = services.get_weather("London")
    if weather_report:
        print(weather_report)

    # Example: Fetch data from another API
    api_url = "https://jsonplaceholder.typicode.com/posts"
    api_data = services.get_data_from_api(api_url)
    if api_data:
        print(api_data[:2])  # Print the first two items of the fetched data
