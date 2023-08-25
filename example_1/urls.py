from django.urls import path
from .views import webcam, workarea, statistics,dashboard, ipcam#, #detectme#,run_webcam#, ipcam#, update
# from .views import webcam, run_webcam
from .views import webcam_view
urlpatterns = [
    ####################################################
    path('', webcam, name='user-webcam'),
    path('statistics/', statistics, name='user-statistics'),
    path('workarea/', workarea, name='user-workarea'),
    path("dashboard/", dashboard, name = "user-dashboard"),
    # path("detectme/", detectme, name = "detectme"),
    path('webcam/', webcam_view, name='webcam'),
    ####################################################


    # path("", run_webcam, name='user-runwebcam'),
    # path('webcam/', webcam, name='webcam'),
    
    path("ip/", ipcam, name = "ip-cam")
    # path('update/<str:msg>', update, name='update-home')
]