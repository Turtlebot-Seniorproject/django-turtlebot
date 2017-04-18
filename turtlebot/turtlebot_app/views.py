from django.shortcuts import render
from . import turtlebot_adaptors


def home(request):
    if request.method == "POST":
        location_id = request.POST.get("destination", "")
        turtlebot_adaptors.establish_connection_and_send_destination(location_id)    
    return render(request, "turtlebot_app/home.html")
