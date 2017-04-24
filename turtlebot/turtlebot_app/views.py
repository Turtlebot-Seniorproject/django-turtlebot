from django.shortcuts import render
from . import turtlebot_adaptors
import csu_constants


def home(request):
    if request.method == "POST":
        location_id = request.POST.get("destination", "")
        ip = request.POST.get("IP", "")
        location_id = _get_named_rooms(location_id)
        turtlebot_adaptors.establish_connection_and_send_destination(location_id, ip)    
    return render(request, "turtlebot_app/home.html")

def _get_named_rooms(location_id=None):
    if location_id:
        if location_id == "Foxes Den":
            return "130"
        #add other room definitions here.
        #this could be a dictionary but I would like to add user-auth
    else:
        return "ERROR"
