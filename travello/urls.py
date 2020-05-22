from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import subscribeViewSet

#router = DefaultRouter()
#router.register('subscribe',subscribeViewSet ,basename='subscribe')


urlpatterns = [
    #path('Api/subscribe',include(router.urls)),
    #path('Api/subscribe/<int:pk>', include(router.urls)),
    path('', views.index, name= 'index'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('temprature', views.temprature, name='temprature'),
    path('discription',views.discription,name='discription'),
    path('subscribe',views.subscribed,name='subscribed'),
    path('book', views.book, name='book'),
    path('Api/Destination/<int:pk>',views.GenericAPIDestination.as_view()),
    path('Api/Destination', views.GenericAPIDestination.as_view()),
    path('Api/subscribe', views.subscribeViewSet.as_view()),
    path('Api/subscribe/<int:pk>', views.subscribeViewSet.as_view()),
]
