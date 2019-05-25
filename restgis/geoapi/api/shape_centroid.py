from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from osgeo import ogr; ogr.UseExceptions()

# urls.py: path('api/shape/centroid', shape_centroid.view)

@api_view(['POST'])
def view(request):
    
    input_str_geojson = request.body.decode('utf-8')
    
    ogr_geom = ogr.CreateGeometryFromJson(input_str_geojson)
    
    ogr_point = ogr_geom.Centroid()
    
    raw_json = ogr_point.ExportToJson()
    
    return Response(json.loads(raw_json))
