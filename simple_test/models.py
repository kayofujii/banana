import uuid
from enum import Enum

from django.db import models


class CandidateTestResult(models.Model):
    class TestType(Enum):
        BIG5 = ("big5", "BIG5性格テスト")

        @classmethod
        def get_value(cls, member):
            return cls[member].value

    data = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=[x.value for x in TestType], blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 後で追加
    # candidate = models.ForeignKey(
    #     Candidate, related_name="test_result", on_delete=models.CASCADE, blank=True, null=True
    # )
