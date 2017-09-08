from django.shortcuts import render
import logging
from webapp import  forms
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse

logger = logging.getLogger(__name__)

# Create your views here.

def login_page(request):
    if (request.method == "POST"):
        if ("username" in request.POST.keys()):
            signup_input = forms.Signup(request.POST)
            if signup_input.is_valid():
                data = signup_input.clean()
            else:
                error_msg = signup_input.errors
                return JsonResponse(error_msg)
        else:
            signin_input = forms.Signin(request.POST)
            if signin_input.is_valid():
                data = signin_input.clean()
            else:
                error_msg = signin_input.errors
                return render(request, 'index.html', {'errors': error_msg})
    else:
        return render(request,'index.html')
def home_page():
    pass