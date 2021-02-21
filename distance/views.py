from django.shortcuts import render, get_object_or_404

from .forms import MeasurementModelForm
from .models import Measurement
from .utils import get_ip_address, get_geo
from geopy.geocoders import Photon
from geopy.distance import geodesic


def calculate_distance_view(request):
    # initial values
    distance = None
    destination = None

    geolocator = Photon(user_agent='distance', timeout=10)
    form = MeasurementModelForm(request.POST or None)

    obj = get_object_or_404(Measurement, id=1)
    ip_ = get_ip_address(request)
    ip = '46.216.43.208'
    lat, lon = get_geo(ip)  # In production app will use 'ip_'
    location = geolocator.geocode(ip)

    # location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)

        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        instance.location = location
        instance.distance = distance
        instance.save()

    context = {
        'distance': distance,
        'destination': destination,
        'form': form,
    }

    return destination
