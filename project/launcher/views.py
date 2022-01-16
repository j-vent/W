from django.shortcuts import render
from launcher.models import Housing
# Create your views here.


def index(request):
    all_shelters = Housing.objects.all()

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
        
        # TODO: Change the HTML to be rendered to something else?
        return render(request, 'my_filter.html', context)

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