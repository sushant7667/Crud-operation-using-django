from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.

#country state view
@api_view(['GET'])
def countryData(request):
        item=countrymodel.objects.all()
        country_serializer=Countryserializer(item,many=True)
        stateitem=statemodel.objects.all()
        state_serializer=Stateserializer(stateitem,many=True)
        Response_ = {
            "countryList":country_serializer.data,
            "stateList":state_serializer.data,
            "response":{
                "n":1,
                "msg":"Data found succefully",
                "Status":"Success"
            }
        }
        return Response(Response_)


@api_view(['POST'])
def getstate(request):
        getdata=request.POST.get('countryId')
        print(getdata)
        item=statemodel.objects.filter(country_id=getdata) 
        serializer=Stateserializer(item,many=True)
        print(serializer.data)
        return Response(serializer.data)

#Employee view
@api_view(['POST'])
def testAdd(request):
    data={}
    data['name'] = request.POST.get('name')
    data ['midname'] = request.POST.get ('midname')
    data ['surname'] = request.POST.get ('surname')
    data ['countryId'] = request.POST.get ('countryId')
    data ['stateId'] = request.POST.get ('stateId')
    data ['mobile_no'] = request.POST.get ('mobile_no')
    data ['email'] = request.POST.get ('email')
    # crudNameObject = testCrud.objects.filter(isactive=True,name=request.POST.get('name')).first()
    # crudMidNameObject = testCrud.objects.filter(isactive=True,midname=request.POST.get('midname')).first()
    # crudSurNameObject = testCrud.objects.filter(isactive=True,surname=request.POST.get('surname')).first()
    # crudCountryObject = testCrud.objects.filter(isactive=True,countryId=request.POST.get('countryId')).first()
    # crudstateObject = testCrud.objects.filter(isactive=True,stateId=request.POST.get('stateId')).first()
    
    
    #validation
    crudNoObject = testCrud.objects.filter(isactive=True,mobile_no=request.POST.get('mobile_no')).first()
    crudEmailObject = testCrud.objects.filter(isactive=True,email=request.POST.get('email')).first()
    crudObjectValidation = ['crudNoObject','crudEmailObject']

    #condition   for validation 
    if crudObjectValidation is not None:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"User with this Mobile Number/ Email id/ name/ midname already exists",
                "Status":"Failed"

            }
        }
        return Response(Response_)
  

    serializer=testcruserializerapi(data=data)
    if serializer.is_valid():
        serializer.save()
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"Data has been stored successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":serializer.errors,
            "response":{
                "n":0,
                "msg":"Error saving data",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['POST'])
def UserAdd(request):
    data={}
    data['Firstname'] = request.POST.get('Firstname')  
    data['Lastname'] = request.POST.get('Lastname')
    data['mobile_no'] = request.POST.get('mobile_no')
    data['gender'] = request.POST.get('gender')
    data['email'] = request.POST.get('email')
    data['address'] = request.POST.get('address')
    data['countryId'] = request.POST.get('countryId')
    data['stateId'] = request.POST.get('stateId')
    data['image'] = request.FILES.get('image')
    data['dateofbirth'] = request.POST.get('dateofbirth')
    data['dateofjoining'] = request.POST.get('dateofjoining')


    print("data",data)
    #validation
    crudNoObject = Employeecrud.objects.filter(isactive=True,mobile_no=request.POST.get('mobile_no')).first()
    crudEmailObject = Employeecrud.objects.filter(isactive=True,email=request.POST.get('email')).first()
    # crudObjectValidation = ['crudEmailObject'],['crudEmailObject']

    #condition   for validation 
    if crudNoObject is not None:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"User with this Mobile Number/ Email id already exists",
                "Status":"Failed"

            }
        }
        return Response(Response_)

    if crudEmailObject is not None:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"User with this Mobile Number/ Email id already exists",
                "Status":"Failed"

            }
        }
        return Response(Response_)

    serializer=Userserializer(data=data)
    # print("serializer",serializer)

    if serializer.is_valid():
        serializer.save()
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"Data has been stored successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":serializer.errors,
            "response":{
                "n":0,
                "msg":"Error saving data",
                "Status":"Failed"

            }
        }
        return Response(Response_)




@api_view(['GET'])
def getAllUsers(request):
    getUserObject =  Employeecrud.objects.filter(isactive=True)
    if getUserObject is not None:
        #Userserializer used for countryID from serializer.py class
        serializer = Userserializer(getUserObject,many=True)
        for i in serializer.data:
            print("i",i['countryId'] ,"j",i['stateId'])
            if i['countryId'] and i['stateId'] is not None:
                countryName = countrymodel.objects.filter(id=i['countryId']).first()
                statename = statemodel.objects.filter(id=i['stateId']).first()
                i['countryId'] = countryName.cname
                i['stateId'] = statename.sname
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"Data has been found successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No data found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['GET'])
def getUserid(request,id):
    individualData = []
    getUserObject =  Employeecrud.objects.filter(isactive=True,id=id).first()
    if getUserObject is not None:
        serializer = Userserializer(getUserObject)
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"Data has been found successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No data found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['POST'])
def updateUser(request,id):
    getUserObject =  Employeecrud.objects.filter(isactive=True,id=id).first()
    #in if satement uopdate/("show") previous data means user entered already and then update
    if getUserObject is not None:
        data={}
        data['Firstname'] = request.POST.get('Firstname')  
        data['Lastname'] = request.POST.get('Lastname')
        data['mobile_no'] = request.POST.get('mobile_no')
        data['gender'] = request.POST.get('gender')
        data['email'] = request.POST.get('email')
        data['address'] = request.POST.get('address')
        data['countryId'] = request.POST.get('countryId')
        data['stateId'] = request.POST.get('stateId')
        data['image'] = request.FILES.get('image')
        data['dateofbirth'] = request.POST.get('dateofbirth')
        data['dateofjoining'] = request.POST.get('dateofjoining')
        print("back api data",data)
        serializer = Userserializer(getUserObject,data=data)
        # #validation
        # validemail = Employeecrud.objects.filter(isactive=True,email = request.POST.get('email')).exclude(id=id).first() 
        # validno = Employeecrud.objects.filter(isactive=True,mobile_no = request.POST.get('mobile_no')).exclude(id=id).first()
        # validation = [Employeecrud.email,validemail,validno]
        # print ("validation",validation)
        # if getUserObject.email == data ['email'] and validemail is not None:
        #     Response_ = {
        #     "data":{},
        #     "response":{
        #         "n":0,
        #         "msg":"User with this email Id already exists",
        #         "Status":"Failed"

        #     }
        #     }
        #     return Response(Response_)
    # else:
        if serializer.is_valid():
            serializer.save()
            print("save",serializer.data)
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "msg":"User Data has been Updated successfully",
                    "Status":"Success"

                }
            }
            return Response(Response_)
            # else:
            #     print("err",serializer.errors)
            #     Response_ = {
            #         "data":serializer.errors,
            #         "response":{
            #             "n":0,
            #             "msg":"Error updating User",
            #             "Status":"Success"

            #         }
            #     }
            #     return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"User not Found",
                "Status":"Failed"

            }
        }
        return Response(Response_)


@api_view(['GET'])
def deleteUser(request,id):
    getUserObject =  Employeecrud.objects.filter(isactive=True,id=id).first()
    if getUserObject is not None:
        data ={}
        data['isactive'] = False
        serializer = Userserializer(getUserObject,data=data)
        if serializer.is_valid():
            serializer.save()
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "msg":"User has been deleted successfully",
                    "Status":"Success"

                }
            }
            return Response(Response_)
        else:
            Response_ = {
            "data":serializer.errors,
            "response":{
                "n":0,
                "msg":"Error Deleting Data",
                "Status":"Failed"

                }
            }
            return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No data found",
                "Status":"Failed"

            }
        }
        return Response(Response_)




#checkbox
@api_view(['POST'])
def checkboxadd(request):
    data={}
    data['boxname'] = request.POST.get('boxname') 
    print ("data",data)           
    serializer=checkboxserializer(data=data)
    print ("serializer",serializer)
    if serializer.is_valid():
        serializer.save() 
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "Status":"Success",
                "msg":"added successfully"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":serializer.errors,
            "response":{
                "n":0,
                "Status":"Failed",
                "msg":"unsucessful"
            }
        }
        return Response(Response_)


@api_view(['POST'])
def checkboxupdate(request,id):
    UpdateUserObject = checkbox.objects.filter(isactive=True,id=id).first()
    if UpdateUserObject is not None:
        data={}
        data['boxname'] = request.POST.get('boxname')   
        print("data",data)
        serializer = checkboxserializer(UpdateUserObject,data=data)
        if serializer.is_valid():
            serializer.save() 
            Response_ = {
                "Roledata":serializer.data,
                "response":{
                    "n":1,
                    "Status":"Success",
                    "msg":"update successfully"

                }
            }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No role found",
                "Status":"Failed"
            }
        }
        return Response(Response_)


@api_view(['GET'])
def getcheckbox(request):
    getuserobject = checkbox.objects.filter(isactive=True)
    if getuserobject is not None:
        serializer = checkboxserializer(getuserobject,many=True)
        Response_ = {
            "GetDatarole":serializer.data,
            "response":{
                "n":1,
                "msg":"role found successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No role found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

@api_view(['GET'])
def getcheckboxid (request,id):
    getuserobject = checkbox.objects.filter(isactive=True,id=id).first()
    if getuserobject is not None:
        serializer = checkboxserializer(getuserobject)
        Response_ = {
            "roledata":serializer.data,
            "response":{
                "n":1,
                "msg":"role found successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No role found",
                "Status":"Failed"

            }
        }
        return Response(Response_)


@api_view(['GET'])
def Deletecheckbox(request,id):
    userobject = checkbox.objects.filter(id=id,isactive=True).first()
    if userobject is not None:
        data = {}
        data ['isactive'] = False 
        serializer = checkboxserializer(userobject,data=data)
        if serializer.is_valid():
            serializer.save()
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "msg":"Role deleted successfully",
                    "Status":"Success"

                }
            }
            return Response(Response_)
        else:
            Response_ = {
            "data":serializer.errors,
            "response":{
                "n":0,
                "msg":"Error Deleting Role",
                "Status":"Failed"

                }
            }
            return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No Role found",
                "Status":"Failed"

            }
        }
        return Response(Response_)

#checkbox all data get
@api_view(['GET'])
def checkboxData(request):
        item=checkbox.objects.all()
        checkbox_serializer=checkboxserializer(item,many=True)
        Response_ = {
            "checkboxlist":checkbox_serializer.data,
            "response":{
                "n":1,
                "msg":"Data found succefully",
                "Status":"Success"
            }
        }
        return Response(Response_)



#check box many to many

@api_view(['POST'])
def hobbiesadd(request):
    data={}
    data['boxname_id'] = request.POST.get('boxname_id')      
    data['hobbies_id'] = request.POST.getlist('hobbies_id')
    checkbhoxobj = checkboxmany.objects.filter(boxname_id=data['boxname_id']).first()
    if  checkbhoxobj is not None:
        # userializer = Permissionserializer(permissionobj, data=data)
        # if userializer.is_valid():
        #     userializer.save() 
        # print ("datassss",data)
        serializer=hobbiesserializer(checkbhoxobj,data=data)
        if serializer.is_valid():
            serializer.save() 
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "Status":"Success",
                    "msg":"permission saved successfully"

                }
            }
            return Response(Response_)
        else:
            Response_ = {
                "data":serializer.errors,
                "response":{
                    "n":0,
                    "Status":"Failed",
                    "msg":"unsucessful"
                }
            }
            return Response(Response_)
    else:
        serializer=hobbiesserializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            Response_ = {
                "data":serializer.data,
                "response":{
                    "n":1,
                    "Status":"Success",
                    "msg":"permission saved successfully"

                }
            }
            return Response(Response_)
        else:
            Response_ = {
                "data":serializer.errors,
                "response":{
                    "n":0,
                    "Status":"Failed",
                    "msg":"unsucessful"
                }
            }
            return Response(Response_)


@api_view(['GET'])
def hobbiesdetails(request):
    item = checkboxmany.objects.all()
    serializer = hobbiesserializer(item,many=True)
    Response_ = {
        "Gethobbies":serializer.data,
        "response":{
            "n":1,
            "msg":"Data found succefully",
            "Status":"Success"
        }
    }
    return Response(Response_)




