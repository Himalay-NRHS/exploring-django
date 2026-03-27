from django.shortcuts import render
from django.utils.html import escape

# Create your views here.

def vulnerable_view(request):
    name =""
    if request.method=='POST':
        name = request.POST.get("name")
        #name = escape(name)

    return render(request,"vulnerable.html",{"name":name})