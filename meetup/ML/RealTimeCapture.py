import os
import threading
import time

import pyshark as pyshark
import psutil


class RealTimeCapture:
    @staticmethod
    def getInterface():
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
