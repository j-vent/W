from django.shortcuts import render
from launcher.models import Housing
from .filters import HousingFilter
import csv
# Create your views here.


def index(request):
    # TODO: load csv data into our housing model -- is this for a particular day??
    # TODO: get best housing options 
    housing = Housing.objects.all() # get complete list of housing
    # TODO: additional filtering of housing objects in db based on user requests (i.e. they want something < 2 km and has showers)
    # TODO: link to Google Maps API so we have a visual of these places
    context = {
        'housing': housing,
    }

    # send request to the index page with the housing data passed in
    return render(request, 'index.html', context)

# Try to filter stuff here (MVP) 
def search(request):
    # with open('/Users/cheetey/Documents/Winter2022/W/project/launcher/test_model.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)
    distance = request.GET.get("distance")
    print("Distance provided: " + distance)

    housing_list_from_db = Housing.objects.all()
    
    # Loop thru the dataset and save those shelters that are within the range into "within_dist"
    within_distance_shelter_names = []

    # Distance parameter is provided
    if distance:
        with open('/Users/cheetey/Documents/Winter2022/W/project/launcher/test_model.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[3])
                if int(row[3]) <= int(distance):
                    # print("row: " + row[3] " and distance: " + distance)
                    within_distance_shelter_names.append(row[0])

    # Distance parameter is not provided
    else:
        within_distance_shelter_names = housing_list_from_db
    print(within_distance_shelter_names)

    housing_filter = HousingFilter(request.GET, queryset=housing_list_from_db)
    context = {
        'filter': housing_filter,
        'distance': within_distance_shelter_names
    }
    return render(request, 'index.html', context)