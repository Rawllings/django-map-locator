from django.shortcuts import render
import folium

# Create your views here.

def index(request):
    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([-1.2497, 36.9451], tooltip='Click for more', popup="Chokaa").add_to(m)
    # Get HTML Representation of Map    
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'index.html', context)


# Latitude: -1.286389
# Longitude: 36.817223