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

    # TODO: additional filtering of housing objects in db based on user requests (i.e. lgbtq+ friendly and has showers)
    # add chee code

    # TODO: get actual distance from user
    distance_param = 2
    within_distance_shelters = []

    for house in housing:
        # print('lat ', house.latitude)
        # print('lon ', house.longitude)
        dest_lat = str(house.latitude)
        dest_lon = str(house.longitude)
        # TODO: replace origins with google maps geolocator coordinates (ryan's code)
        # orig_lat = original latitude val
        # orig_lon = original longitude val
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=53.56764,-113.48694&destinations="+ dest_lat +","+ dest_lon +"&units=metric&key="+settings.GOOGLE_API_KEY
        payload={}
        headers = {}

        # extract json
        response = requests.request("GET", url, headers=headers, data=payload)
        jsonResponse = response.json()
        
        # parse json
        distance = jsonResponse['rows'][0]['elements'][0]['distance']['text']
        print("distance json response ", distance)
        distance_val = float(distance.split(" ")[0])

        if (distance_val <= distance_param):
            within_distance_shelters.append({'name':house.shelter_name,
            'address': house.address,
            'capacity': house.capacity})

    print("items in within dist", within_distance_shelters)
    # TODO: filter within distance shelter by other fields (Chee code)

    context = {
        'housing': within_distance_shelters,
        'google_api_key': settings.GOOGLE_API_KEY,
        'lat_0': 53.55511,
        'lon_0' : -113.48496,
        'res' : response
        
    }
    print("in view!")

    # send request to the index page with the housing data passed in
    return render(request, 'index.html', context)