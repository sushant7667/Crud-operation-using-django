from django.shortcuts import render,redirect
from . import views
from rest_framework.decorators import api_view
from .models import *
import requests
from rest_framework.response import Response
from django.contrib import messages


# Create your views here.

#urls 

#countryurl
countryurl = 'http://127.0.0.1:8000/Registaration/countryData'


#emp urls
UserAddurl = 'http://127.0.0.1:8000/Registaration/UserAdd'
getAllUsersurl = 'http://127.0.0.1:8000/Registaration/getAllUsers'
getUseridurl = 'http://127.0.0.1:8000/Registaration/getUserid/'
updateUserurl = 'http://127.0.0.1:8000/Registaration/updateUser/'
deleteUserurl = 'http://127.0.0.1:8000/Registaration/deleteUser/'



#emp front 

def UserAddfront(request):
        if request.method == "POST":
                data={}
                data['Firstname'] = request.POST.get('Firstname')  
                data['Lastname'] = request.POST.get('Lastname')
                data['mobile_no'] = request.POST.get('mobile_no')
                data['gender'] = request.POST.get('gender')
                data['email'] = request.POST.get('email')
                data['address'] = request.POST.get('address')
                data['countryId'] = request.POST.get('countryId')
                data['stateId'] = request.POST.get('stateId')
                data['dateofbirth'] = request.POST.get('dateofbirth')
                data['dateofjoining'] = request.POST.get('dateofjoining')
                # print ("dataaaaa",data)
                files= {}
                files['image'] = request.FILES.get('image') 
                print ("files",files)     
                print ("dataaaaa",data)
                responseUrl = requests.post(UserAddurl,data=data , files=files)
                result = responseUrl.json()
                print("result",result)
                if result['response']['n'] == 1:
                        messages.success(request, result['response']['msg'])
                        return redirect('Frontapp:getUserempfront')
                else:
                        messages.error(request, result['response']['msg'])
                        return redirect('Frontapp:getUserempfront') 
        else:
                countryresponse = requests.get(countryurl)
                countryData = countryresponse.json()
                return render(request,'add-list.html',{'countryList':countryData['countryList'],'stateList':countryData['stateList']})

def getUserempfront(request):
        response = requests.get(getAllUsersurl)
        geodata = response.json()
        return render(request,'view.html',{'GetData':geodata['data']})  


def updateUserfront(request,id):
        if request.method == "GET":
                getUser = getUseridurl + str(id)
                response = requests.get(getUser)
                geodata = response.json()
                countryresponse = requests.get(countryurl)
                countryData = countryresponse.json()
                return render(request,'update.html',{'GetData':geodata['data'],'countryList':countryData['countryList'],'stateList':countryData['stateList']})
        else:
                data={}
                data['Firstname'] = request.POST.get('Firstname')  
                data['Lastname'] = request.POST.get('Lastname')
                data['mobile_no'] = request.POST.get('mobile_no')
                data['gender'] = request.POST.get('gender')
                data['email'] = request.POST.get('email')
                data['address'] = request.POST.get('address')
                data['countryId'] = request.POST.get('countryId')
                data['stateId'] = request.POST.get('stateId')
                data['dateofbirth'] = request.POST.get('dateofbirth')
                data['dateofjoining'] = request.POST.get('dateofjoining')
                files= {}
                files['image'] = request.FILES.get('image') 
                print ("files",files) 
                print ("data",data)
                updateUser = updateUserurl + str(id)
                responseUrl = requests.post(updateUser,data=data,files=files)
                result = responseUrl.json()
                print("result",result)
                if result['response']['n'] == 1:
                        messages.success(request, result['response']['msg'])
                        return redirect('Frontapp:getUserempfront')
                else:
                        messages.error(request, result['response']['msg'])
                        return redirect('Frontapp:getUserempfront') 

def deletedata(request,id):
        deleteSubdata=deleteUserurl + str(id)
        delete_UserUrl = requests.get(deleteSubdata)
        result = delete_UserUrl.json()
        print ("result",result)
        # return redirect('deleted successfully')
        if result['response']['n'] == 1:
                messages.success(request, result['response']['msg'])
                return redirect('Frontapp:getUserempfront')
        else:
                messages.error(request, result['response']['msg'])
                return redirect('Frontapp:getUserempfront') 

