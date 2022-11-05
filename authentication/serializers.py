from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data) :
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("please rewrite the password correctly")
        if len(data.get('password1')) < 4:
            raise serializers.ValidationError("password should be 4 characters or more")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password1']
        )
        return user