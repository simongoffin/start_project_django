from django.shortcuts import render
from django.http import HttpResponse
import json
import logging

# Create your views here.

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def home(request):
    return render(request, 'load/home.html')

def progress(request):
    if request.method == 'POST':
        percent = int(request.POST['state']) + 10
        response_data = {}
        response_data['state'] = percent
        logging.info('Percent = %s !!!'%percent)
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        logging.error("nothing to see")
        return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}), content_type="application/json")
