from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from simple_test.models import CandidateTestResult

from .serializers import TestResultSerializer


class TestResultListApiView(APIView):
    def get(self, request):
        results = CandidateTestResult.objects.all()
        serializer = TestResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        result_data = {
            "data": request.data.get("data"),
            "type": request.data.get("type"),
            "token": request.data.get("token"),
        }
        serializer = TestResultSerializer(data=result_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestResultDetailApiView(APIView):
    def get_object(self, result_id):
        try:
            return CandidateTestResult.objects.get(id=result_id)
        except CandidateTestResult.DoesNotExist:
            return None

    def get(self, request, result_id):
        result_instance = self.get_object(result_id)
        if not result_instance:
            return Response({"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TestResultSerializer(result_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, result_id):
        result_instance = self.get_object(result_id)
        if not result_instance:
            return Response({"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        result_data = {
            "data": request.data.get("data"),
            "type": request.data.get("type"),
            "token": request.data.get("token"),
        }
        serializer = TestResultSerializer(instance=result_instance, data=result_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, result_id):
        result_instance = self.get_object(result_id)
        if not result_instance:
            return Response({"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        result_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
