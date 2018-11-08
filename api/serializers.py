from datasource.models import Complaint
from rest_framework import serializers


class ComplaintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complaint
        fields = ('record_number', 'record_type', 'record_type_map', 'record_type_desc', 'description',
                  'open_date', 'last_inspected_date', 'last_inspected_result', 'status', 'original_address',
                  'original_city', 'original_state', 'original_zip', 'complaint_link', 'latitude',
                  'longitude', 'url')
