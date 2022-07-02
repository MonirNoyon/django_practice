from .models import Student
from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StuSerializer(serializers.Serializer):
    name = serializers.CharField(
        label=_("name"),
        write_only=True
    )

    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        name = attrs.get('name')

        if name :
            user = authenticate(request=self.context.get('request'),
                                name=name)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')


        extra_kwargs = {
            "password" :{"write_only":True},
            "email":{
                "required":True,
                "allow_blank":True,
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(), "email Already exists"
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = User.objects.create(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        return user