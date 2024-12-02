from django.shortcuts import render
from django.http import HttpResponse

from radikolite_home import utils


def index(request):
    
    stations = utils.get_radio_stations()
    
    return HttpResponse(stations)
