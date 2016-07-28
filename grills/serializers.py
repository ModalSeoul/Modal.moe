from grills.models import Grill
from rest_framework import serializers


class GrillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grill
