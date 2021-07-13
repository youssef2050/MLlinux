import json
import threading
import time

from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, Http404
from django.core import serializers
from meetup.ML.CICFlowMeterFeatures.GetFeatures import convertToCSV
from meetup.ML.RealTimeCapture import RealTimeCapture
from meetup.ML.BGTs import BGTs
from django.shortcuts import render

from meetup.models import Files, ResultML

x = True


def index(request):
    result = RealTimeCapture.getInterface
    return render(request, 'meetups/index.html', {'result': result})


def runTime(request, interface):
    if interface == 'offline':
        return render(request, 'meetups/uploadFile.html')
    else:
        return render(request, 'meetups/result.html', {
            'title': interface,
            'close': False,
        })


def runLiveCapture(request):
    if request.is_ajax and request.method == "POST":
        runCapture(request.POST.get('interface'), 3600, True)
        return JsonResponse({'massage': 'run capture'}, safe=False)
    else:
        return Http404


def runCapture(interface, timeout, loop):
    print(interface)
    local_time = time.time()
    RealTimeCapture.liveCapture(interface, local_time, timeout)
    file = Files(name=local_time, slug=str(local_time), file='files/' + str(local_time) + '.pcap')
    file.save()
    time.sleep(timeout - 15)
    if loop:
        runCapture(interface, timeout, x)


def stopCapture(request):
    if request.is_ajax and request.method == "POST":
        convertToCSV('uploads/files/csv/vpn_test.csv')
        global x
        x = False
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


def uploadFiles(request):
    local_time = time.time()
    for file in request.FILES:
        print(file)
        fs = FileSystemStorage()
        fs.save(str(local_time) + '.pcap', request.FILES[file])
        fileData = Files(name=local_time, slug=str(local_time), file=str(local_time) + '.pcap')
        fileData.save()
    return JsonResponse({'massage': 'uploaded!'}, safe=False)
    # return JsonResponse({'massage': 'error'}, safe=False)
