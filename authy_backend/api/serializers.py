from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User


class CustomTokenObtainPairSerrializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)

            if not user.check_password(password):
                raise Exception('No active account found with the given credentials')
            

            if not user.is_active:
                raise Exception ('Account is inactive')
            

        except User.DoesNotExist:
            raise Exception('No active account found with the given credentials')
       
       
        data =  super().validate(attrs)

        return data
    


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ("username",'email',"password","password2")

        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise Exception('password do not match')
        
        return data
        
    def create(self, validated_data):
        validated_data.pop('password2')

        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('username', 'email')