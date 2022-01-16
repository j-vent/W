from django.shortcuts import render
from launcher.models import Housing
from django.conf import settings
import requests

import logging


# Create your views here.


def index(request):
    all_shelters = Housing.objects.all()

    # TODO: get actual distance from user
    distance_param = 4
    within_distance_shelters = []

    if (request.method == "POST"):
        lgbtq2s_friendly = request.POST.get("lgbtq2s_friendly")
        if lgbtq2s_friendly:
            print("lgbtq2s")
            all_shelters = all_shelters.filter(lgbtq2s_friendly=1)

        wheelchair_accessible = request.POST.get("wheelchair_accessible")
        if wheelchair_accessible:
            print("wheelchair")
            all_shelters = all_shelters.filter(wheelchair_accessible=1)

        public_transit_accessible = request.POST.get("public_transit_accessible")    
        if public_transit_accessible:
            print("public_transit")
            all_shelters = all_shelters.filter(public_transit_accessible=1)

        women_only = request.POST.get("women_only")    
        if women_only:
            print("women_only")
            all_shelters = all_shelters.filter(women_only=1)

        food_provided = request.POST.get("food_provided")
        if food_provided:
            print("food")
            all_shelters = all_shelters.filter(food_provided=1)

        showers_provided = request.POST.get("showers_provided")
        if showers_provided:
            print("showers")
            all_shelters = all_shelters.filter(showers_provided=1)

        context = {
            "all_shelters": all_shelters
        }

        for house in all_shelters:
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
                within_distance_shelters.append({'shelter_name':house.shelter_name,
                'address': house.address,
                'capacity': house.capacity})

        print("items in within dist", within_distance_shelters)
        # TODO: filter within distance shelter by other fields (Chee code)

        context = {
            'all_shelters': within_distance_shelters,
            'google_api_key': settings.GOOGLE_API_KEY,
            'lat_0': 53.55511,
            'lon_0' : -113.48496,
            
        }
        # TODO: Change the HTML to be rendered to something else?
        return render(request, 'my_filter.html', context)

    # TODO: load csv data into our housing model -- is this for a particular day??
    # TODO: get best housing options 
    # housing = Housing.objects.all() # get complete list of housing

    # TODO: additional filtering of housing objects in db based on user requests (i.e. lgbtq+ friendly and has showers)
    # add chee code

    # TODO: get actual distance from user
    # distance_param = 2
    # within_distance_shelters = []

    # for house in housing:
    #     # print('lat ', house.latitude)
    #     # print('lon ', house.longitude)
    #     dest_lat = str(house.latitude)
    #     dest_lon = str(house.longitude)
    #     # TODO: replace origins with google maps geolocator coordinates (ryan's code)
    #     # orig_lat = original latitude val
    #     # orig_lon = original longitude val
    #     url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=53.56764,-113.48694&destinations="+ dest_lat +","+ dest_lon +"&units=metric&key="+settings.GOOGLE_API_KEY
    #     payload={}
    #     headers = {}

    #     # extract json
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     jsonResponse = response.json()
        
    #     # parse json
    #     distance = jsonResponse['rows'][0]['elements'][0]['distance']['text']
    #     print("distance json response ", distance)
    #     distance_val = float(distance.split(" ")[0])

    #     if (distance_val <= distance_param):
    #         within_distance_shelters.append({'name':house.shelter_name,
    #         'address': house.address,
    #         'capacity': house.capacity})

    # print("items in within dist", within_distance_shelters)
    # # TODO: filter within distance shelter by other fields (Chee code)

    context = {
        'housing': within_distance_shelters,
        'google_api_key': settings.GOOGLE_API_KEY,
        'lat_0': 53.55511,
        'lon_0' : -113.48496,
       
    }
    print("in view!")

    # send request to the index page with the housing data passed in
    return render(request, 'index.html', context)