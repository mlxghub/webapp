from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def login_page(request):
    return render(request, 'index.html')

def home_page():
    pass