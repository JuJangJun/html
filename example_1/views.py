from django.shortcuts import render

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import threading

# import pandas as pd

import cv2

from check import check_v4
from example_1 import open_cam
from example_1 import ip_cam

# from check_v4 import Model


# Create your views here.
# def home(request):
#     context = {'msg':'여기에 check의 return값 뿌려주자'}
#     return render(request, 'example_1/home.html', context)

####################################################
import torch
import torchvision
from torchvision import transforms

# resize_trans = transforms.Compose([
#     transforms.Resize((368,368)),
#     transforms.ToTensor()
# ])



def webcam_view(request):
    return render(request, 'example_1/webcam.html')

#수정방향
def webcam(request):
    # img = torchvision.datasets.imageFolder(root = "check/3.jpg" , transform = resize_trans)
    img = cv2.imread("check/3.jpg")
    # img = cv2.imread(ip_cam.IpCam.cam_2('http://192.168.0.174:8080/shot.jpg'))
    # img = ip_cam.IpCam.cam_2('http://192.168.0.174:8080/shot.jpg') #ipcam으로 연결하는 코드 해당코드를 살리면서 테스트를 진행할시에 ipcam또한 실행중이여야한다.
    # context = {'msg':check_v4.Model.calculate(img)["wc"]}
    context = check_v4.Model.calculate(img)
    return render(request, 'example_1/webcam.html', context)
    # return render(request, 'example_1/webcam.html', context),render(request, 'example_1/webcam.html', context1) 

def statistics(request):
    return render(request, 'example_1/statistics.html')

def workarea(request):
    return render(request, 'example_1/workArea.html')

def dashboard(request):
    return render(request, 'example_1/index.html')
####################################################



# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target = self.update, args = ()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode(".jpg", image)
#         return jpeg.tobytes()
    
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @gzip.gzip_page
# def detectme(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type = "multipart/x-mixed-replace;boundary = frame")
#     except:
#         print("에러입니다.")
#         pass


# def run_webcam(request):
#     context = {'cam':open_cam.Cam.cam_1()}
#     return render(request, 'example_1/home.html', context)

# def webcam(request):
#     # img = cv2.imread("check/3.jpg")
#     img = cv2.imread(open_cam.Cam.cam_1())
#     context = {'msg':check_v4.Model.calculate(img)}
#     return render(request, 'example_1/home.html', context)



def ipcam(request):
    context =  ip_cam.IpCam.cam_2('http://192.168.0.174:8080/shot.jpg')
    return render(request, 'example_1/webcam.html', context)

# def update(request, msg):
#     context = {'msg':msg}
#     return render(request, 'user/home.html', context)