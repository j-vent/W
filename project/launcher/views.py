from django.shortcuts import render
from launcher.models import Housing
from django.conf import settings
import requests

import logging


# Create your views here.


def index(request):
    # TODO: load csv data into our housing model -- is this for a particular day??
    # TODO: get best housing options 
    housing = Housing.objects.all() # get complete list of housing
    # TODO: additional filtering of housing objects in db based on user requests (i.e. they want something < 2 km and has showers)
    # TODO: link to Google Maps API so we have a visual of these places
    logging.basicConfig(level = logging.INFO)
    logging.warning("fuc")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key="+settings.GOOGLE_API_KEY
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    for key, value in response.text.items():
        print(key, value)
    context = {
        'housing': housing,
        'google_api_key': settings.GOOGLE_API_KEY,
        'lat_0': 53.55511,
        'lon_0' : -113.48496,
        'res' : response
    }
    print("in view!")
   
    

    

    # send request to the index page with the housing data passed in
    return render(request, 'index.html', context)