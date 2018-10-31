from django.core.management.base import BaseCommand
from datasource.models import Complaint
import csv


class Command(BaseCommand):
    help = 'Import Complaints from a csv file.'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="File path")

    def handle(self, *args, **options):
        file_path = options['path']
        with open(file_path, mode='r') as data:
            data_dict = csv.DictReader(data)
            line_count = 0
            for row in data_dict:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                new_complaint, created = Complaint.objects.get_or_create(
                    record_number=row['RecordNum'],
                    record_type=row['RecordType'],
                    record_type_map=row['RecordTypeMapped'],
                    record_type_desc=row['RecordTypeDesc'],
                    description=row['Description'],
                    open_date=row['OpenDate'] or None,
                    last_inspected_date=row['LastInspDate'] or None,
                    last_inspected_result=row['LastInspResult'],
                    status=row['StatusCurrent'],
                    original_address=row['OriginalAddress1'],
                    original_city=row['OriginalCity'],
                    original_state=row['OriginalState'],
                    original_zip=row['OriginalZip'],
                    complaint_link=row['Link'],
                    latitude=row['Latitude'] or None,
                    longitude=row['Longitude'] or None,
                )
                line_count += 1
            print(f'Processed {line_count} lines.')
