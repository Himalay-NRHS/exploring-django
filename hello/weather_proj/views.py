# from django.shortcuts import render



# # Create your views here.
from django.shortcuts import render
import requests 


API_KEY = "11a82ee838f331090da6b899389e4471"
# API_KEY = "8074e31092f386b21a55f4bef8c3a5ac"

def weather_view(request):
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
            }
        else:
            error = "Invalid city name. Please try again."

    return render(request, "weather.html", {
        "weather": weather_data,
        "error": error
    })