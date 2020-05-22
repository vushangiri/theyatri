from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Destination,subscribe,bookings
from django.contrib import messages
from travello.serializer import DestinationSerial,subscribeSerial
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import requests



# Create your views here.
def temprature(request):
        city= request.POST['city_data']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e97bb1eb01dcd766c9703c75b2014009'
        r = requests.get(url.format(city)).json()
        city_weather = {
                'discription' : r['weather'][0]['description'],
                'city' : city,
                'temp' : r['main']['temp']-273,
                'feels_like' : r['main']['feels_like'],
                'temp_min' : r['main']['temp_min'],
                'temp_max' : r['main']['temp_max'],
                'pressure' : r['main']['pressure'],
        }
        context = {'city_weather' : city_weather}
        return render(request,'temprature.html',context)

def contact(request):
    return render(request, 'travel/contact.html')

def index(request):

    dest= Destination.objects.all()

    return render(request,'travel/index.html',{'dest': dest})
def search(request):
    name = request.POST['name']
    if Destination.objects.filter(name=name).exists():
        dawa = Destination.objects.all()
        dest_data = Destination.objects.get(name=name)
        return render(request, 'search.html', {'dest_data' : dest_data,'dawa' : dawa})
    else:
        return render(request, 'error.html')

@login_required(login_url='login')
def discription(request):
    desc_1= request.GET['field']
    data_1= Destination.objects.get(name=desc_1)
    data2 =Destination.objects.all()
    return render(request,'destination_details.html', {'desc_1': data_1,'data2':data2})
def subscribed(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        Subscribe = subscribe.objects.create(email=email)
        Subscribe.save()
        return redirect('/')
    else:
        return render(request,'destination_details.html')
def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        plocation = request.POST['plocation']
        destination = request.POST['destination']
        phone = request.POST['phone']
        date = request.POST['date']
        hour = request.POST['hour']
        min = request.POST['min']
        zone= request.POST['zone']
        book_flight = bookings.objects.create(name=name,email=email,plocation=plocation,destination=destination,phone=phone,date=date,hour=hour,min=min,zone=zone)
        book_flight.save()
        booki = bookings.objects.all()
        messages.info(request, 'SUCCESSFULLY BOOKED')
        return redirect('/')
    else:
        return render(request,'book.html')
        



    # Generic Class Based Api View

class GenericAPIDestination(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    queryset = Destination.objects.all()
    serializer_class = DestinationSerial
    authentication_classes = [SessionAuthentication, BasicAuthentication ,TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def put(self, request, pk=None):
        if pk:
            return self.update(request, pk)
        else:
            return self.create(request)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class subscribeViewSet(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    queryset = subscribe.objects.all()
    serializer_class = subscribeSerial
    authentication_classes = [SessionAuthentication, BasicAuthentication ,TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def put(self, request, pk=None):
        if pk:
            return self.update(request, pk)
        else:
            return self.create(request)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# from Generic View sets
'''
class subscribeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = subscribe.objects.all()
    serializer_class = subscribeSerial
'''
# from normal viewset
'''class subscribeViewSet(viewsets.ViewSet):
    def list(self,request,pk=None):
        if pk:
            queryset = subscribe.objects.all()
            article = get_object_or_404(queryset, pk=pk)
            sears = subscribeSerial(article)
            return Response(sears.data)
        else:
            serializer = subscribe.objects.all()
            sears = subscribeSerial(serializer, many=True)
            return Response(sears.data)
    def put(self,request,pk=None):
        if pk:
            serializer = subscribeSerial(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        else:
            serializer = subscribeSerial(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
    def delete(self, request,pk):
        queryset = subscribe.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        sears = subscribeSerial(article)
        return Response(status=status.HTTP_204_NO_CONTENT)

'''



'''

    class Newapi(APIView):

        def get(self,request):
            serializer = Article.objects.all()
            sears = ArticleSearilizers(serializer, many=True)
            return Response(sears.data)

        def put(self,request):
                serializer = ArticleSearilizers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_201_CREATED)


    class Articledetail(APIView):
        def get_object(self, id):
            try:
                return Article.objects.get(id=id)

            except Article.DoesNotExist:
                return Response(status=status.HTTP_200_OK)

        def get(self , request , id):
            arc = self.get_object(id)
            serializer = ArticleSearilizers(arc)
            return Response(serializer.data)
        def put(self, request , id):
            serializer = ArticleSearilizers(data=Response.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)

        def delete(self,request,id):
            arc = self.get_object(id)
            arc.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




    '''

'''

    @api_view(['GET', 'POST'])
    def Api(request):
        if request.method == 'GET':
            sear = Article.objects.all()
            sears = ArticleSearilizers(sear,many=True)
            return Response(sears.data)

        elif request.method == 'POST':
            serializer = ArticleSearilizers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
'''
    @csrf_exempt
    def Article_detail(request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            arc = Article.objects.get(pk=pk)

        except Article.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ArticleSearilizers(arc)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ArticleSearilizers(arc, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            arc.delete()
            return HttpResponse(status=204)
    '''

# Api View Method(function)
'''
    @api_view(['GET', 'POST','DELETE'])
    def Article_detail(request, pk):
        """
        Retrieve, update or delete a code Article.
        """
        try:
            arc = Article.objects.get(pk=pk)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_200_OK)

        if request.method == 'GET':
            serializer = ArticleSearilizers(arc)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ArticleSearilizers(data=Response.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            arc.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
         '''




