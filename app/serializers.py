from rest_framework import serializers
from app.models import Records


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('__all__')