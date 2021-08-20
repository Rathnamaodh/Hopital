from rest_framework import serializers
from .models import Hospital, Salesperson, Register, My_Temp,My_upload, Multi,Custom_Files,Pagination




class MultiSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Multi
        fields = '__all__'




# multiple files upload
class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Multi
        fields=['user','image']

# Custom files upload

class CustomFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_Files
        # fields = '__all__'
        fields=['id','user','profile_pic','aadhar_pic','xl_file']



# Multiple images upload

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model =My_upload
        fields = ['id','user','aadhar_image','pancard_image']

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class SalespersonSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source='user.id')
    # user = serializers.ReadOnlyField(source='user.username')
    # Hospital_id = serializers.ReadOnlyField(source='hospital.id')
    # Hospital_name = serializers.ReadOnlyField(source='hospital.name')

    class Meta:
        model = Salesperson
        # fields = ['user','user_id', 'Hospital_id', 'Hospital_name']
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    # Hospital_name = serializers.ReadOnlyField(source='hospital.salesperson.id')
    # user_id = serializers.ReadOnlyField(source='user.id')
    # user = serializers.ReadOnlyField(source='user.username')
    # Hospital_id = serializers.ReadOnlyField(source='hospital.id')


    class Meta:
        model = Register
        fields = '__all__'
        # fields = ['user','user_id', 'Hospital_id', 'Hospital_name']


class PaginationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagination
        fields = '__all__'





















class My_TempSerializers(serializers.ModelSerializer):
    # Hospital_id = serializers.ReadOnlyField(source='hospital.id')
    Alocated_hospital_name = serializers.ReadOnlyField(source='hospital.name')

    allocated_salesperson = serializers.ReadOnlyField(source='salesperson.user.username')
    allocated_salesperson_id = serializers.ReadOnlyField(source='salesperson.user.id')

    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    selected_hospital = serializers.ReadOnlyField(source='salesperson.hospital.name')






    class Meta:
        model = My_Temp
        fields = ['user','user_id','allocated_salesperson','allocated_salesperson_id','Alocated_hospital_name','selected_hospital','address','state']
        # fields = '__all__'


















#*********************************************************************************************8


from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user










