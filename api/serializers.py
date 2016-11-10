from rest_framework import serializers
from expeditions.models import Expedition, Waypoint, Registration
from django.contrib.auth.models import User
from accounts.models import Profile
from djoser import settings
from django.db import transaction


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user','id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'date_joined')


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'date_joined', 'email', 'id', 'is_staff')
        read_only_fields = ('username', 'id', 'date_joined', 'is_staff')


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True,
                                     validators=settings.get('PASSWORD_VALIDATORS'))

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            User._meta.pk.name,
            'password',
            'email'
        )

    def create(self, validated_data):
        if settings.get('SEND_ACTIVATION_EMAIL'):
            with transaction.atomic():
                user = User.objects.create_user(**validated_data)
                user.is_active = False
                user.save(update_fields=['is_active'])
        else:
            user = User.objects.create_user(**validated_data)
        return user


class ExpeditionSerializer(serializers.ModelSerializer):
    waypoints = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # registrations = serializers.HyperlinkedIdentityField(view_name='expeditionregistration-list')
    class Meta:
        model = Expedition
        fields = '__all__'


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ('registration_number', 'user')
