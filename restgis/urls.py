from django.urls import path

from .geoapi.api import test_api
from .geoapi.api import shape_centroid
from .geoapi.api import shape_crop

urlpatterns = [
    path('api/test', test_api.test_view),
    
    path('api/shape/centroid', shape_centroid.view),
    
    path('api/shape/crop', shape_crop.view),
]
