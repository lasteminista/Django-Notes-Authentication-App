from django.urls import path
from mynotesapp import views

urlpatterns =[
	path('',views.home, name='home'),
]
