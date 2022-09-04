from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from app.models import Records
from app.serializers import RecordsSerializer


class RecordsApiView(APIView):

    def get(self, request):
        records = Records.objects.all()
        serializer = RecordsSerializer(instance=records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RecordsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class RecordsDetailApiView(APIView):
    def get_objects(self, records_id):
        try:
            return Records.objects.get(id=records_id)
        except Records.DoesNotExist:
            return None

    def get(self, request, records_id):
        records = self.get_objects(records_id)
        serializer = RecordsSerializer(records)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, records_id):
        records = self.get_objects(records_id)
        serializer = RecordsSerializer(records, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request, records_id):
        records = self.get_objects(records_id)
        records.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, records_id):
        records = self.get_objects(records_id)
        serializer = RecordsSerializer(instance=records, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
