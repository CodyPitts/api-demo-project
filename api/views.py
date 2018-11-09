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

    """
    List a queryset, but adding some querystring functionality.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if request.GET.get('filter_type_map', ''):
            queryset = queryset.filter(record_type_map=request.GET.get('filter_type_map'))
        if request.GET.get('sort', '').lower() == 'asc':
            queryset = queryset.order_by('open_date')
        if request.GET.get('sort', '').lower() == 'desc':
            queryset = queryset.order_by('-open_date')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)