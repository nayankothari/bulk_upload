from django.urls import path, include
from .views import UploadFile


urlpatterns = [ 
    path('upload-files', UploadFile.as_view(), name="upload-files"),
]