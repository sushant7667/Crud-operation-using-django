from django.urls import path,include
from django.contrib import admin
from Frontapp import views


urlpatterns = [
    path('UserAddfront', views.UserAddfront,name="UserAddfront"),
    path('getUserempfront', views.getUserempfront,name="getUserempfront"),
    path('updateUserfront/<int:id>', views.updateUserfront,name="updateUserfront"),
    path('deletedata/<int:id>', views.deletedata,name="deletedata"),

]