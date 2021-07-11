import json
import threading
import time

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, Http404
from django.core import serializers
from meetup.ML.CICFlowMeterFeatures.GetFeatures import convertToCSV
from meetup.ML.RealTimeCapture import RealTimeCapture
from meetup.ML.BGTs import BGTs
from django.shortcuts import render

from meetup.models import Files, ResultML


def index(request):
    # runCapture('ens33',20,200)
    # convertToCSV('uploads/files/csv/vpn_test.csv')
    # result= BGTs.predict([[658,1,1,33,345,33,33,33,0,345,345,345,0,574468.09,3039.51,658,0,658,658,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1519.76,1519.76,33,345,137,180.13,32448,0,0,0,0,0,0,0,0,1,205.5,33,345,0,0,0,0,0,0,0,16,0,172,0,0,0,8,0,0,0,0,1.43E+15,0,1.43E+15,1.43E+15]])
    result = RealTimeCapture.getInterface
    return render(request, 'meetups/index.html', {'result': result})


def runTime(request, interface):
    if interface == 'offline':
        return render(request, 'meetups/uploadFile.html')
    else:
        runCapture(interface, 500)
        return render(request, 'meetups/result.html', {
            'title': interface,
            'close': False,
        })


def runLiveCapture(request):
    if request.is_ajax and request.method == "POST":
        runCapture(request.POST.get('interface'), 5000)
        return JsonResponse({'massage': 'run capture'}, safe=False)
    else:
        return Http404


def runCapture(interface, timeout):
    print(interface)
    local_time = time.time()
    RealTimeCapture.liveCapture(interface, local_time, timeout)
    file = Files(name=local_time, slug=str(local_time), file='files/' + str(local_time) + '.pcap')
    file.save()


def stopCapture(request):
    if request.is_ajax and request.method == "POST":
        RealTimeCapture.closeCapture()
        data = ResultML.objects.all().values('ip_src', 'port_src', 'ip_des', 'port_des', 'classification')
        return JsonResponse({'data': list(data),
                             'massage': 'stop capture',
                             'close': False
                             }, safe=False)
    else:
        return Http404


def getData(request):
    if request.is_ajax and request.method == "POST":
        data = ResultML.objects.all().values('ip_src', 'port_src', 'ip_des', 'port_des', 'classification')
        return JsonResponse({'data': list(data)}, safe=False)
    else:
        return Http404
