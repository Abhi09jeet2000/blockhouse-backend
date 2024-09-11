import json
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
## We also can read json file from json directory but for now kept simple

def getCandleStickData(request):
 try:

  return HttpResponse(
         json.dumps({
          "data":[
           {"time": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
           {"time": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40}
          ],
          "status": status.HTTP_200_OK
         }),
         headers={"content-type": "application/json"}
        )
 except:
   return HttpResponse({
    "status": status.HTTP_400_BAD_REQUEST
   })


def getLineChartData(request):
 try:
  return HttpResponse(
         json.dumps({
            "labels": ["Jan", "Feb", "Mar", "Apr"],
            "data": [10, 20, 30, 40],
            "status": status.HTTP_200_OK
         }),
         headers={"content-type": "application/json"}
       )
 except:
   return HttpResponse({
    "status": status.HTTP_400_BAD_REQUEST
   })


def getBarChartData(request):
 try:
  return HttpResponse(
         json.dumps({
          "labels": ["Product A", "Product B", "Product C"],
          "data": [100, 150, 200],
          "status": status.HTTP_200_OK
         }),
         headers={"content-type": "application/json"}
        )
 except:
   return HttpResponse({
    "status": status.HTTP_400_BAD_REQUEST
   })

def getPieChartData(request):
 try:
  return HttpResponse(
         json.dumps({
          "labels": ["Red", "Blue", "Yellow"],
          "data": [300, 50, 100],
          "status": status.HTTP_200_OK
         }),
         headers={"content-type": "application/json"}
        )
 except:
   return HttpResponse({
    "status": status.HTTP_400_BAD_REQUEST
   })

