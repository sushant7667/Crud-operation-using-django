from django.urls import path,include
from django.contrib import admin
from Registaration  import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #countrystate api
    # path('CountryName', views.CountryName,name="CountryName"),
    # path('StateName', views.StateName,name="StateName"),
    #country state
    path("countryData", views.countryData,name="countryData"),
    path("getstate", views.getstate,name="getstate"),


#
    path("UserAdd", views.UserAdd,name="UserAdd"),
    path("getAllUsers", views.getAllUsers,name="getAllUsers"),
    path("getUserid/<int:id>", views.getUserid,name="getUserid"),
    path("updateUser/<int:id>", views.updateUser,name="updateUser"),
    path("deleteUser/<int:id>", views.deleteUser,name="deleteUser"),


#checkbox
    path("checkboxadd", views.checkboxadd,name="checkboxadd"),
    path("checkboxupdate/<int:id>", views.checkboxupdate,name="checkboxupdate"),
    path('getcheckbox', views.getcheckbox,name="getcheckbox"),
    path('getcheckboxid/<int:id>', views.getcheckboxid,name="getcheckboxid"),
    path('Deletecheckbox/<int:id>', views.Deletecheckbox,name="Deletecheckbox"),
    path('checkboxData', views.checkboxData,name="checkboxData"),



#hobbies 

    path('hobbiesadd', views.hobbiesadd,name="hobbiesadd"),
    path('hobbiesdetails', views.hobbiesdetails,name="hobbiesdetails"),
]
