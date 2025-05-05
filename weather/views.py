import requests
from django.shortcuts import render
from django.conf import settings

def weather_home(request):
    """
    View to display the current weather for a given city.
    """
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            # Add icon URL for frontend
            weather_data['icon_url'] = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png"
        except requests.exceptions.RequestException:
            error = 'Invalid city name or API error. Please try again.'

    return render(request, 'weather/weather_home.html', {
        'weather_data': weather_data,
        'error': error,
    })

def weather_forecast(request):
    """
    View to display the 5-day weather forecast for a given city.
    """
    forecast_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()
            forecast_data = response.json()
            # Filter for daily noon forecasts and add icon URLs
            forecast_data['filtered_list'] = [
                item for item in forecast_data['list'] if item['dt_txt'].endswith('12:00:00')
            ]
            for item in forecast_data['filtered_list']:
                item['icon_url'] = f"http://openweathermap.org/img/wn/{item['weather'][0]['icon']}@2x.png"
        except requests.exceptions.RequestException:
            error = 'Invalid city name or API error. Please try again.'

    return render(request, 'weather/weather_forecast.html', {
        'forecast_data': forecast_data,
        'error': error,
    })