import geocoder#for gps location
import pyowm as owm




owm = owm.OWM("917f044a319c58ae297a11390d9f998a")  # You MUST provide a valid API key
def getLocation():
    locationINPUT = ("London,GB")
    location = owm.weather_at_place(locationINPUT)
    return location
def getWeather(location):
    global wind
    global weather
    global humidity
    global temperture
    weather = location.get_weather()
    wind = weather.get_wind()
    humidity = weather.get_humidity()              # 87
    temperature = weather.get_temperature('fahrenheit')












location = getLocation()
getWeather(location)
print("wind: " + str(wind))
print("temperature: " + temperature)
print("wind: " + str(wind))
