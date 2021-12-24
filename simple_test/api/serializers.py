from django.contrib.auth.models import User
from rest_framework import serializers
from simple_test.models import CandidateTestResult


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTestResult
        fields = ["data", "type", "token"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "password")
        extra_kwargs = {"password": {"write_only": True, "style": {"input_type": "password"}}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        return super().update(instance, validated_data)
