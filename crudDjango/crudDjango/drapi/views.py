from django.shortcuts import render
from . models import Aiquest
from  . serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
# Queryset
def aiquest_info(request):
    # complex data
    ai = Aiquest.objects.all()
    # python dictionary
    serializer = AiquestSerializer(ai, many=True)
    # render json data
    json_data = JSONRenderer().render(serializer.data)
    # return json data
    return HttpResponse(json_data, content_type='application/json')



def aiquest_ins(request, pk):
    # complex data
    ai = Aiquest.objects.get(id=pk)
    # python dictionary
    serializer = AiquestSerializer(ai)
    # render json data
    json_data = JSONRenderer().render(serializer.data)
    # return json data
    return HttpResponse(json_data, content_type='application/json')