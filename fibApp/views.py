from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from .searlizers import fibSerailizers

class calFib(APIView):

    def post(self, request, format=None):
        print(request.data)

        #number= int(request.number)
        number=int(request.data["number"])

        if number < 0:
            return Response({'message': 'please enter a valid number'})
        else:
             sequence=fibonacci(number)
             request.data['time']=sequence[0]
             serializer = fibSerailizers(data=request.data)
             if serializer.is_valid():
                 serializer.save()
             return Response({'message': str(sequence[1]) + ' as the ' + str(number) + 'th element in the sequence','total_time_taken':sequence[0]},
                        status=status.HTTP_201_CREATED)
        return Response({'message': 'please enter a valid number'})





class index(APIView):
    def post(self, request, format=None):
        print(request.data)
        list1 = ['pankaj', 'kumar']
        output = ', '.join(list1)
        return HttpResponse(output)


def calculateTime(func):
    def inner(n):
        start_time= time.time()
        sequence=func(n)
        end_time= time.time()
        total_time=end_time-start_time
        return (total_time,sequence)
    return inner

@calculateTime
def fibonacci(number):
    a = 0
    b = 1
    if number < 0:
        print("Incorrect input")
    elif number == 0:
        return a
    elif number == 1:
        return b
    else:
        for i in range(1,number):
            c = a + b
            a = b
            b = c
        return b