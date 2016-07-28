from grills.models import Grill
from rest_framework import viewsets
from grills.serializers import GrillSerializer


class GrillViewSet(viewsets.ModelViewSet):
    """ API endpoint. Just lists the grills. """
    queryset = Grill.objects.all()
    serializer_class = GrillSerializer
