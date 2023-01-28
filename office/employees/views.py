from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employees.serializers import EmployeeRegistrationSerializer, EmployeeLoginSerializer, EmployeeProfileSerializer, EmployeeChangePasswordSerializer, EmployeePersonalInfoSerializer
from employees.models import EmployeePersonalInfo
from django.contrib.auth import authenticate
from employees.renderers import EmployeeRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Generating Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user) 

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class EmployeeRegistrationView(APIView):
    renderer_classes = [EmployeeRenderer]
    def post(self, request, format=None):
        serialzer = EmployeeRegistrationSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            employee = serialzer.save()
            token = get_tokens_for_user(employee)
            return Response({'token':token,'msg':'Registration Successfull'},status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeLoginView(APIView):
    renderer_classes = [EmployeeRenderer]
    # permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = EmployeeLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            employee=authenticate(email=email, password=password)
            if employee is not None:
                token = get_tokens_for_user(employee)
                return Response({'token':token, 'msg':'Logged In Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class EmployeeChangePasswordView(APIView):
    renderer_classes = [EmployeeRenderer]
    
    def post(self, request, format=None):
        serializer = EmployeeChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeePersonalInfoView(APIView):
    renderer_classes = [EmployeeRenderer]
    
    def post(self, request, format=None):
        serializer = EmployeePersonalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Profile Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'fields_errors'}, status=status.HTTP_206_PARTIAL_CONTENT)
        
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            employee_info = EmployeePersonalInfo.objects.get(user=id)
            serializer = EmployeeProfileSerializer(employee_info)
            return Response({'profile':serializer.data})
        employee_info = EmployeePersonalInfo.objects.all()
        serializer = EmployeeProfileSerializer(employee_info, many=True)
        return Response({'all_profile':serializer.data})
    
    def put(self, request, pk, format=None):
        id=pk
        employee_info = EmployeePersonalInfo.objects.get(user=id)
        serializer = EmployeeProfileSerializer(employee_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Profile Updated'}, status=status.HTTP_202_ACCEPTED)
        return Response({'error':'fields_errors'}, status=status.HTTP_206_PARTIAL_CONTENT)
    
    def patch(self, request, pk, format=None):
        id=pk
        employee_info = EmployeePersonalInfo.objects.get(user=id)
        serializer = EmployeeProfileSerializer(employee_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Profile Updated'}, status=status.HTTP_202_ACCEPTED)
        return Response({'error':'fields_errors'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        id = pk
        if id is not None:
            employee_info = EmployeePersonalInfo.objects.get(pk=id)
            employee_info.delete()
            return Response({'msg':'Data Deleted'})
        return Response({'error':'Employee doesn"t" exist'}, status=status.HTTP_400_BAD_REQUEST)
