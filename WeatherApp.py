 # Weather-App-CLI
import urllib.request
import urllib.parse
import json
from datetime import datetime


def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search?"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    url += urllib.parse.urlencode(params)


    try:

        response = urllib.request.urlopen(url)

        data = json.loads(response.read())


        if "results" not in data:
            return None


        result = data["results"][0]


        return (
            result["latitude"],
            result["longitude"],
            result["name"],
            result["country"]
        )


    except:

        return None




def get_weather(lat, lon):


    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&current_weather=true"
    )


    try:

        response = urllib.request.urlopen(url)

        return json.loads(response.read())


    except:

        return None




def main():


    print("""
============================
       WEATHER CLI APP
============================
""")


    while True:


        city = input(
            "Enter city name (exit to quit): "
        )


        if city.lower() == "exit":

            print("Goodbye 🌦️")

            break



        location = get_coordinates(city)



        if location is None:

            print("❌ City not found")

            continue



        weather = get_weather(
            location[0],
            location[1]
        )



        if weather:


            current = weather["current_weather"]


            print("\n==========================")

            print(
                f"🌍 {location[2]}, {location[3]}"
            )


            print(
                f"🌡 Temperature: {current['temperature']} °C"
            )


            print(
                f"💨 Wind Speed: {current['windspeed']} km/h"
            )


            print(
                f"🕒 Time: {datetime.now()}"
            )


            print("==========================\n")



        else:

            print("Weather unavailable")




if __name__ == "__main__":

    main()