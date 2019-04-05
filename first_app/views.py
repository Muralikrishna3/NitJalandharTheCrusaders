from django.shortcuts import render
from django.http import HttpResponse
import argparse
import datetime
import imutils
import math
import cv2
import numpy as np
from .PeopleCounterMain import start, getLength, stopVideo
# Create your views here.

# global variables
camera = cv2.VideoCapture("test2.mp4")
width = 800
textIn = 0
textOut = 0

# main start
firstFrame = None
leng=1;

def testIntersectionIn(x, y):
    res = -450 * x + 400 * y + 157500
    if ((res >= -550) and (res < 550)):
        print(str(res))
        return True
    return False

def testIntersectionOut(x, y):
    res = -450 * x + 400 * y + 180000
    if ((res >= -550) and (res <= 550)):
        print(str(res))
        return True
    return False

def index(request):
    # Processing
    print('inner index')
    leng='starting'
    return render(request, 'first_app/index.html', {'length': leng})

# cleanup the camera and close any open windows
# camera.release()
# cv2.destroyAllWindows()
def startFunction(request):
    start()
    return HttpResponse("video stopped in start function")

def stopFunction(request):
    stopVideo()
    return HttpResponse("video stopped")

def updateLength(request):
    leng=getLength()
    return HttpResponse(leng)
