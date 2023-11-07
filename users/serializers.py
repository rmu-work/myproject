from django.contrib.auth import authenticate, login
from rest_framework import serializers
from users.models import User
import requests

def generate_id():
    import random

    first = random.randint(100, 999)
    second = random.randint(100, 999)

    uni_id = f'UNI{first}{second}'

    if User.objects.filter(university_id=uni_id).exists():
        generate_id()
    else:
        return uni_id



class StudentRegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # 'username',
            'password',

            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'contact_number',
            'residency_status',
            'portfolio',

            'profile_picture',
            'country',
            'state',
            'address'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'], last_name=validated_data['last_name'],
            email=validated_data['email'], date_of_birth=validated_data['date_of_birth'],
            contact_number=validated_data['contact_number'], residency_status=validated_data['residency_status'],
            portfolio=validated_data['portfolio'], country=validated_data['country'],
            state=validated_data['state'], address=validated_data['address'],
            profile_picture=validated_data['profile_picture'], username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentRegisterRetrieveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',

            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'contact_number',
            'residency_status',
            'portfolio',

            'profile_picture',
            'country',
            'state',
            'address'
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(LoginSerializer, self).__init__(*args, **kwargs)

    def validate(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = authenticate(self.request, username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        self.user = user # noqa

        return validated_data

    def login(self, request):
        if hasattr(self, 'user'):
            login(request, self.user)
            return self.user


class UniversitySerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(required=True)

    def validate(self, attrs):
        university_name = attrs.get('university_name', None)

        if not self.instance:
            if User.objects.filter(university_name=university_name).exists():
                raise serializers.ValidationError({
                    'university_name': 'University already exist.'
                })

        return attrs


    class Meta:
        model = User
        fields = (
            'email',
            'contact_number',

            'university_id',
            'university_name',
            'website',

            'country',
            'state',
            'address',
        )

    def create(self, validated_data):
        university_id = generate_id()
        name = validated_data['university_name']
        username = name.replace(" ", '').lower()
        university = User.objects.create(
            university_id=university_id, email=validated_data['email'],
            contact_number=validated_data['contact_number'],
            university_name=validated_data['university_name'],
            website=validated_data['website'], is_university=True,
            country=validated_data['country'], state=validated_data['state'],
            address=validated_data['address'], username=username
        )
        return university


class UniversityRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

