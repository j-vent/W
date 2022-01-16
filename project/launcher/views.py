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
    logging.basicConfig(level = logging.INFO)
    logging.warning("fuc")


    # TODO: change the origins coordinates, destination coordinates will be from the database
    # TODO: loop through the housing db -- look for the houses returned by csv in the database and get their coordinates
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=53.56764,-113.48694&destinations=53.55019,-113.49134&units=metric&key="+settings.GOOGLE_API_KEY
    payload={}
    headers = {}

    # extract json
    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = response.json()
    # print(response.text)
    # for key, value in jsonResponse.items():
    #     print(key, value)
    
    distance = jsonResponse['rows'][0]['elements'][0]['distance']['text']
    print("distance json response ", distance)
    distance_val = distance.split(" ")[0]


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