from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile
from djoser import settings


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user','id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'date_joined')


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