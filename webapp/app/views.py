from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        contex = {
            'name': 'rishi'
        }
        # return render(request, "home.html", context=contex)
        return Response(contex)
