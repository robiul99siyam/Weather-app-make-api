from rest_framework import viewsets
from .models import Description
from .serailzer import DescriptionSerailzer

class DescriptionViewsets(viewsets.ReadOnlyModelViewSet):
    """ make a description viewset here """

    queryset = Description.objects.all()
    serializer_class = DescriptionSerailzer