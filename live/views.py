from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from django.views.generic import ListView
import json

# Create your views here.
# def home(request):
# 	data = Service.objects.all()
# 	return render(request, "main.html", {'context': data})

class InfoListView(ListView):
    model = Service
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #convert python dictionary to Json
        context["qs_json"] = json.dumps(list(Service.objects.values()))   
        return context

