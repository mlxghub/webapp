from django.shortcuts import render
import logging
from webapp import  forms
logger = logging.getLogger(__name__)

# Create your views here.
def login_page(request):
    if (request.method == "POST"):
        if ("username" in request.POST.keys()):
            signup_input = forms.Signup(request.POST)
            if signup_input.is_valid():
                data = signup_input.clean()
                print(data)
            else:
                error_msg = signup_input.errors
                return render(request,'index.html',{'errors':error_msg})
        else:
            pass
    else:
        return render(request,'index.html')
def home_page():
    pass