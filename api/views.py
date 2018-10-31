from datasource.models import Complaint
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ComplaintSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'complaints': reverse('complaint-list', request=request, format=format)
    })


class ComplaintViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
