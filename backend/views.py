from django.shortcuts import render
from django.http import HttpResponse
import subprocess, requests
from subprocess import Popen
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from backend.settings import BACKEND_PHP_SERVER
from backend.utils import get_device_id

def index(request):
    if request.method == "POST":
        if "email" not in request.POST.keys() or not request.POST["email"]:
            print("no email in keys")
            return render(
                request, "backend/home.html", {"error": "You need to provide an email"}
            )

        if "password" not in request.POST.keys() or not request.POST["password"]:
            print("password")
            return render(
                request, "backend/home.html", {"error": "You need to provide an email"}
            )

        payload = {
            "email": request.POST["email"],
            "password": request.POST["password"],
            "machine_id": get_device_id()
        }
        print("the payload is ", payload)
        # response = requests.post(f"{BACKEND_PHP_SERVER}/login/", payload)
        return render(request, "backend/success.html", {})
    else:
        return render(request, "backend/home.html")
