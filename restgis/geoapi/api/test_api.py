from rest_framework.decorators import api_view
from rest_framework.response import Response

# urls.py: path('api/test', test_api.test_view)

@api_view(['GET'])
def test_view(request):
    return Response({'data': 'OK'})
