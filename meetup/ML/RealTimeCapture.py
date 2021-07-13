import os
import threading
import time

import pyshark as pyshark
import psutil

from meetup.ML.CICFlowMeterFeatures import GetFeatures


class RealTimeCapture:
    @staticmethod
    def getInterface():
        # GetFeatures.convertToCSV('uploads/files/csv/test.csv')
        address = psutil.net_if_addrs()
        address.__setitem__('offline', 'Youssef Ezz-Eldeen Developer ML use python, Android and desktop use java')
        return address.keys()

    @staticmethod
    def liveCapture(interface, outputFilePath, timeout=3600):
        stream = os.popen(
            'timeout ' + str(timeout) + ' tcpdump -w uploads/files/' + str(outputFilePath) + '.pcap -i ' + interface)
        print(stream)

    @staticmethod
    def closeCapture():
        pass
