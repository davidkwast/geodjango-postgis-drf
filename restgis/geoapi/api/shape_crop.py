from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings
import tempfile
import json
from pathlib import Path
import numpy as np
import rasterio
import rasterio.mask
from rasterio.vrt import WarpedVRT

# urls.py: path('api/shape/crop', shape_crop.view)

@api_view(['POST'])
def view(request):
    
    input_geojson = json.loads(request.body)
    
    tci_rasterio = rasterio.open(settings.DEMO_IMAGE_SATELITE_FS_PATH)
    tci_rasterio_dataset = WarpedVRT(tci_rasterio, crs='EPSG:4326')
    
    tci_array, tci_affine = rasterio.mask.mask(
        tci_rasterio_dataset,
        [input_geojson],
        indexes = None,
        crop = True,
        all_touched = False,
        invert = False,
        nodata = 0, #np.nan,
        filled = True,
        pad = False,
    )
    
    tci_x_size, tci_y_size = tci_array.shape[2], tci_array.shape[1] # Z,Y,X
    
    with tempfile.TemporaryDirectory() as tmpdirname:
    
        tci_image_path = Path(tmpdirname).joinpath('tci.png')
        
        with rasterio.open(
            tci_image_path, 'w', driver='PNG',       
            dtype = 'uint8', count = 4,
            width = tci_x_size, height = tci_y_size,
            transform = tci_affine
        ) as tci_rast_fd:
            
            tci_rast_fd.write(tci_array[0], 1)
            tci_rast_fd.write(tci_array[1], 2)
            tci_rast_fd.write(tci_array[2], 3)
            tci_rast_fd.write(
                np.asarray(
                    np.where(tci_array[0] > 0, 255, 0),
                    dtype = np.uint8
                ),
                4
            )
            
        with open(tci_image_path ,'rb') as fd:
            payload = fd.read()
    
    return Response(payload, content_type='image/png')
