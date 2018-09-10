from rest_framework import viewsets
from LogRFID.models import Log
from LogRFID.serializers import LogSerializer
from rest_framework import permissions


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = (permissions.AllowAny,)