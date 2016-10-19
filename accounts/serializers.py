from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='profile-detail')

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'profile', )
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'write_only': True}}
        read_only_fields = ('profile',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_staff', 'is_active', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
