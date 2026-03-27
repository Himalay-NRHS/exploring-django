from django.urls import path,include
from . import views
urlpatterns= [
    path('',views.biodata_form , name='biodata_form'),
]