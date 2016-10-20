from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile


# class UserSerializer(serializers.ModelSerializer):
#     region = serializers.URLField(source='profile.region', allow_blank=True)
#     pc = serializers.URLField(source='profile.pc', allow_blank=False)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'region', 'pc' )
#         extra_kwargs = {'password': {'write_only': True},
#                         'email': {'write_only': True}}
#         read_only_fields = ('profile',)
#
#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


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
        read_only_fields = ('user',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    region = serializers.CharField(source='profile.region', allow_blank=True)
    pc = serializers.BooleanField(source='profile.pc')

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'region', 'pc')
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = super(UserSerializer, self).create(validated_data)
        self.create_or_update_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = Profile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(UserSerializer, self).update(profile, profile_data)