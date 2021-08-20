from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Hospital, Salesperson, Register,My_Temp,My_upload, Multi,Custom_Files,Pagination
from.serializers import HospitalSerializer, SalespersonSerializer, RegisterSerializer ,My_TempSerializers,\
    UploadSerializer,MultiSerializer,SingleSerializer,CustomFilesSerializer,PaginationSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_jwt.authentication import  JSONWebTokenAuthentication
from rest_framework_simplejwt.backends import TokenBackend

#***********************************************************88****************************************************
#***************************************************************************************************************88

# Task 1
#*******************************************************************
#********************************************
# function based views for Hospital
# crud operations

@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def hospital_list(request):
    serializers = HospitalSerializer(data=request.data)

    if request.method == 'GET':
        hospital = Hospital.objects.all()
        serializers = HospitalSerializer(hospital,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        # serializers = HospitalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def hospital_list_detail(request,pk):
    try:
        hospital = Hospital.objects.get(pk=pk)
    except Hospital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = HospitalSerializer(hospital)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = HospitalSerializer(hospital,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# function based views for sales persons
@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def sales_view(request):

    if request.method == 'GET':
        user = request.user
        print("user name is:", user)
        sales = Salesperson.objects.filter(user=user)


        return Response({'sales': SalespersonSerializer(sales, many=True).data, })

    elif (request.method == 'POST'):
        print(request.data)
        serializers = SalespersonSerializer(data=request.data)
        print(serializers)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



## ***************************************************************************************************
#**************************************************************************************************8*
# Function Based Views for register

@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def register(request):
    # serializers = RegisterSerializer(data=request.data)

    if request.method == 'GET':
        register = Register.objects.all()
        serializers = RegisterSerializer(register, many=True)
        return Response(serializers.data)

    # if request.method == 'GET':
    #     user = request.salesperson
    #     sales = Register.objects.filter(user=user)
    #     return Response({'sales': RegisterSerializer(sales, many=True).data, })
    #
    elif (request.method == 'POST'):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


## ***************************************************************************************************
#**************************************************************************************************8*
# Function Based Views for register

@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def register(request):
    # serializers = RegisterSerializer(data=request.data)

    if request.method == 'GET':
        register = Register.objects.all()
        serializers = RegisterSerializer(register, many=True)
        return Response(serializers.data)

    # if request.method == 'GET':
    #     user = request.salesperson
    #     sales = Register.objects.filter(user=user)
    #     return Response({'sales': RegisterSerializer(sales, many=True).data, })
    #
    elif (request.method == 'POST'):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)






#**********************************************************************
#****************************************************************************


# Task 3

#*************************************************************************************
# Multiple files upload with one single input field

from rest_framework.renderers import MultiPartRenderer,HTMLFormRenderer
from rest_framework.decorators import parser_classes

@api_view(['GET','POST'])
#@renderer_classes([MultiPartRenderer,HTMLFormRenderer])
@parser_classes([MultiPartParser,FormParser])
@authentication_classes([ JWTAuthentication])
@permission_classes([IsAuthenticated])
def myFiles(request):

    if request.user.is_authenticated:

        if request.method == 'GET':
            #um=UserFile.objects.all()
            id=request.user.id
            su=Multi.objects.filter(user=id)

            print(su.values())
            print('----')
            si = SingleSerializer(su,many=True)

            print('$$')



            print('@@@')


            return JsonResponse(si.data,safe=False)



        if request.method=='POST':


            usr=request.user.id
            su=request.data
            multifile = request.FILES.getlist('image')

            print(multifile)


            su['user']=usr

            si=None

            # for x,y in  enumerate(multifile):
            #     su[x]=y

            for x in multifile:
                su['image']=x

                print(su.values)

                si=SingleSerializer(data=su)

                if si.is_valid():
                    print('hello')
                    si.save()
                    print('saved')
                    message={'message':'Data created successfully...'}

                else:
                    message={'message':si.errors}

            return Response(message)


        # if request.method=='POST':
        #
        #
        #     usr=request.user.id
        #     su=request.data
        #     multifile = request.FILES.getlist('docfiles')
        #     # multifile=[x for x in request.FILES.dict().values()]
        #     print(multifile)
        #     #su.setlist('files',multifile)
        #
        #     su['user']=usr
        #     #su['docfiles']=multifile
        #
        #     si=SingleSerializer(data=su)
        #
        #     if si.is_valid():
        #         print('hello')
        #         si.save()
        #         return Response({'message':'Data created successfully...'})
        #     else:
        #         return Response(si.errors)
        #



    else:
        return Response({'message':'No user logged in...'})
#**********************************************************************************8
#************************************************************************************

# url is: m
# Multiple images upload
# extact the user_id from the jwttoken

@api_view(['GET','POST'])
#@renderer_classes([MultiPartRenderer,HTMLFormRenderer])
@parser_classes([MultiPartParser,FormParser])
@authentication_classes([ JWTAuthentication])
@permission_classes([IsAuthenticated])
def mv(request):

    if request.user.is_authenticated:

        if request.method == 'GET':
            id=request.user.id
            images=Multi.objects.filter(user=id)
            serializer = SingleSerializer(images, many=True)

            return JsonResponse(serializer.data,safe=False)



        if request.method=='POST':
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]

            data = {'token': token}

            print(data)

            try:

                valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)

                print(valid_data)

                my_user = valid_data['user_id']

                print(my_user)


            except AuthenticationFailed as v:

                print("error", v)

            res = request.data

            res['user'] = my_user
            multifile = request.FILES.getlist('image')
            my_data = None



            for x in multifile:
                res['image'] = x
                print(res.values)
                my_data = SingleSerializer(data=res)
                print(my_data)

                if my_data.is_valid():
                    print('hello')
                    my_data.save()
                    print('saved')
                    message={'message':'Created'}

                else:
                    msg={'message':my_data.errors}
            return Response(message)
    else:
        return Response({'message':'No user'})






#**************************************************************************************8****
#*********************************************************************************************8

#**************************************************************************
#*************************************************************************
# Custom restricted files upload(restricted files upload)
@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def Custom_images(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            user = request.user
            print("user name is:", user)
            files = Custom_Files.objects.filter(user=user)

            return Response({'files': CustomFilesSerializer(files, many=True).data, })

        elif (request.method == 'POST'):
            usr = request.user.id
            req = request.data
            req['user'] = usr

            #decoding the token

            # token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            # data = {'token': token}
            # print(data)
            # try:
            #     valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
            #     print(valid_data)
            #     my_user = valid_data['user_id']
            #     print(my_user)
            #
            # except AuthenticationFailed as v:
            #     print("error", v)
            #
            # res = request.data
            # res['user'] = my_user

            serializers = CustomFilesSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                print(serializers)
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'No user logged in...'})





#***********************************************




#*************************************************************************

# images
from rest_framework.exceptions import AuthenticationFailed
@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def image_upload(request):
    serializers = UploadSerializer(data=request.data)

    if request.method == 'GET':
        user = request.user
        print("user name is:", user)
        sales = My_upload.objects.filter(user=user)

        return Response({'sales': UploadSerializer(sales, many=True).data, })

    elif(request.method == 'POST'):
        token = request.META.get('HTTP_AUTHORIZATION'," ").split(' ')[1]
        data ={'token':token}
        print(data)
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            print(valid_data)
            my_user = valid_data['user_id']
            print(my_user)

        except AuthenticationFailed as v:
            print("error", v)

        res = request.data
        res['user']=my_user



        serializers = UploadSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def image_upload_detail(request,pk):
    try:
        image_upload = My_upload.objects.get(pk=pk)
    except My_upload.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = UploadSerializer(image_upload)
        return Response(serializers.data)

    # elif request.method == 'PUT':
    #     res = request.data
    #     aadhar_image = image_upload_creation()
    #     pancard_image = image_upload_creation()
    #     uder_id = request.user.id
    #     res ['aadhar_image']=aadhar_image
    #     res['pancard_image']=pancard_image
    #     res['user_id']=uder_id
    #
    #
    #     serializers = UploadSerializer(My_upload,request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}
        print(data)
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
            print(valid_data)
            my_user = valid_data['user_id']
            print(my_user)

        except AuthenticationFailed as v:
            print("error", v)

        res = request.data
        res['user'] = my_user

        serializers = UploadSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    # elif request.method == 'PUT':
    #     token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    #     data = {'token': token}
    #     print(data)
    #     try:
    #         valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    #         print(valid_data)
    #         my_user = valid_data['user_id']
    #         print("my user id:" ,my_user)
    #
    #     except AuthenticationFailed as v:
    #         print("error", v)
    #
    #     res = request.data
    #     res['user'] = my_user
    #     user = request.data
    #     print(user)
    #     serializers = UploadSerializer(image_upload,user)
    #     if my_user!=user:
    #         print("hai")
    #     else:
    #         print("no data")
    #     print("data",user)
    #     print("***********************")
    #     sales = My_upload.objects.filter(user=my_user)
    #     serializers = UploadSerializer(data=sales)
    #
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        image_upload.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









#*********************************************************************
#******************************************************************8
# Task 5
# Pagination view
from rest_framework.pagination import PageNumberPagination
from .pagination import MyPagination
@api_view(['GET',])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def Pagination_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = request.user
            print("user name is:", user)
            paginator = PageNumberPagination()
            paginator.page_size = 4
            person_objects =Pagination.objects.all()
            result_page = paginator.paginate_queryset(person_objects, request)
            serializer = PaginationSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)



    else:
        return Response({'message':'No Pages available...'})








#*******************************************************************************************
#*******************************************************************************************

# Testing
@api_view(['GET','POST'])
def temp_view(request):
    # serializers = TempSerializers(data=request.data)

    if request.method == 'GET':
        user = request.user
        temp = My_Temp.objects.filter(user=user)
        serializers = My_TempSerializers(temp, many=True)
        return Response(serializers.data)

    elif (request.method == 'POST'):

        serializers = My_TempSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics


class RegistrationView(generics.CreateAPIView,generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer





from rest_framework.exceptions import AuthenticationFailed
@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication,])
@permission_classes([IsAuthenticated,])
def vio(request):
    serializers = MultiSerializer(data=request.data)

    if request.method == 'GET':
        # user = request.user
        # print("user name is:", user)
        sales = Multi.objects.all()

        return Response({'sales': MultiSerializer(sales, many=True).data, })


    elif (request.method == 'POST'):

        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]

        data = {'token': token}

        print(data)

        try:

            valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)

            print(valid_data)

            my_user = valid_data['user_id']

            print(my_user)


        except AuthenticationFailed as v:

            print("error", v)

        res = request.data

        res['user'] = my_user

        serializers = MultiSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)