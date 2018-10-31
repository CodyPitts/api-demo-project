from django.db import models

# Create your models here.


class Complaint(models.Model):
    record_number = models.CharField(max_length=20)
    record_type = models.CharField(max_length=30)

    CASE = 'case'
    REQUEST = 'request'
    RECORD_TYPE_MAP_CHOICES = (
        (CASE, 'Case'),
        (REQUEST, 'Request'),
    )
    record_type_map = models.CharField(
        max_length=7,
        choices=RECORD_TYPE_MAP_CHOICES,
        default=REQUEST,
    )

    record_type_desc = models.CharField(max_length=40, blank=True, verbose_name='Record Type Description')
    description = models.TextField(blank=True)
    open_date = models.DateField(blank=True, null=True)
    last_inspected_date = models.DateField(blank=True, null=True)
    last_inspected_result = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=30)
    original_address = models.CharField(max_length=60)
    original_city = models.CharField(max_length=20)

    # This can later be pulled up and imported where needed.
    original_state = models.CharField(
        choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
                 ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'),
                 ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
                 ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'),
                 ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
                 ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
                 ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
                 ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
                 ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
                 ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
                 ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
                 ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
                 ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
                 ('WI', 'Wisconsin'), ('WY', 'Wyoming')],
        max_length=2,
        verbose_name='State',
    )

    original_zip = models.CharField(max_length=5)
    complaint_link = models.URLField(max_length=50, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    @property
    def full_location(self):
        return f'''{self.original_address} {self.original_city}, {self.original_city}
            {self.original_zip}
            ({self.latitude}, {self.longitude})'''

    def __str__(self):
        return self.record_number
