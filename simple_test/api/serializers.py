from rest_framework import serializers
from simple_test.models import CandidateTestResult


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTestResult
        fields = ["data", "type", "token"]
