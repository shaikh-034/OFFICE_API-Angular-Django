from rest_framework import serializers
from employees.models import Employees_data, EmployeePersonalInfo

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    
    # We are writing this becz we need confirm password field in our Registration Request
    password1 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = Employees_data
        fields = ['email', 'tc','password', 'password1']
        # fields = '__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    # Validating Password and Confirm Password While Registration
    def validate(self, data):
        password = data.get('password')
        password1 = data.get('password1')
        if password != password1:
            raise serializers.ValidationError("Password and confirm Password doesn't match")
        return data
    
    def create(self, validate_data):
        return Employees_data.objects.create_user(**validate_data)
    
class EmployeeLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = Employees_data
        fields = ['email', 'password']
        
class EmployeeChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password1 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password1']
        
    def validate(self, attrs):
        password = attrs.get('password')
        password1 = attrs.get('password1')
        user = self.context.get('user')
        if password != password1:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs
        
class EmployeePersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePersonalInfo
        fields = '__all__'
        
class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePersonalInfo
        fields = '__all__'