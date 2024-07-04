from django.shortcuts import render, redirect
from .models import Search
import folium
import geocoder
from .forms import SearchForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)
    # folium.Marker([-1.2497, 36.9451], tooltip='Click for more', 
    #               popup="Chokaa").add_to(m)
    
    folium.Marker([lat, lng], tooltip='Click for more', 
                  popup=country).add_to(m)
    

    # Get HTML Representation of Map    
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form
    }
    return render(request, 'index.html', context)


# Latitude: -1.286389
# Longitude: 36.817223