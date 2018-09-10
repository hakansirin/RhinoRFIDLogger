from rest_framework.serializers import ModelSerializer
from LogRFID.models import Log


class LogSerializer(ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

