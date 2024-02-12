import requests
from win10toast_click import ToastNotifier
from plyer import notification


class WeatherData:
  def __init__(self,api_key, zip_code, country_code):
    self.api_key=api_key
    self.zip_code = zip_code
    self.country_code = country_code
    self.coordinates=None
    self.data=None
    
  def getLongLat(self):
    url= f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code},{self.country_code}&appid={self.api_key}"
    response = requests.get(url)
    if response.status_code == 200:
      response_json=response.json()
      self.coordinates = (response_json['lat'], response_json['lon'])
      return {"success": True, "message": None}
    else:
      error_message = "Failed to retrieve coordinates. Please check your zip code/country code and API key."
      return {"success": False, "message": error_message}

  def getCurrentWeather(self):
    if not self.coordinates:
        return {"success": False, "message": "Coordinates not set."}
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={self.coordinates[0]}&lon={self.coordinates[1]}&appid={self.api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        self.data = response_json['weather']
        if self.data and len(self.data) > 0:
           weather_condition = response_json['weather'][0]
           temp_Kelvin=response_json['main']['temp']
           temp_Celsius=round((temp_Kelvin-273.15),2)
           message = {
            'main': weather_condition['main'],
            'description': weather_condition['description'],
            'icon': weather_condition['icon'],
            'temperature': temp_Celsius  
        }
           return {"success": True, "message": message}
        else:
            # Handle the case where 'weather' data is unavailable
            return {"success": False, "message": "Weather data is not available."}
    else:
        # Handle HTTP errors
        error_message = "Failed to retrieve weather data. Please check your API key and coordinates."
        return {"success": False, "message": error_message}


