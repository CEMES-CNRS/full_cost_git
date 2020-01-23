from pathlib import Path
from django.db import models
from collections import OrderedDict
from full_cost.utils.constants import ACTIVITIES

from lab.models import Record as LRecord
from lab.models import Extraction
from lab.models import Record3Range, RecordOneDate, RecordDate, Record2Range
from simple_history.models import HistoricalRecords

activity_short = Path(__file__).parts[-2]

sub_billings = ACTIVITIES[activity_short]['sub_billings']

class CharfieldNum(models.CharField):
    def to_python(self, value):
        return int(value)

class Experiment(models.Model):
    experiment = models.CharField(max_length=200)
    exp_type = models.CharField(choices=sub_billings, default=sub_billings[0][0], max_length=200)
    def __str__(self):
        return f'{self.experiment}'
    class Meta:
        ordering = ['experiment']
# class Extraction(Extraction):
#     history = HistoricalRecords()

subexps = OrderedDict([('None', ['D3', 'Mult']),
                       ('Sample Preparation', ['LT-U']),
                       ('Imagery/Spectroscopy', ['LT-UHV-S', 'DUF-RT', 'DUF-VT']),
                       ('Maintenance', ['LT-U', 'DUF']),
                       ('Topography', ['LT-UHV-4']),
                       ('Atom-Manipulation', ['LT-UHV-4']),
                       ('Spectrocopy', ['LT-UHV-4']),
                       ('Sample Growth', ['DUF-MBE']),
                       ('Sample/Tip preparation', ['DUF-Prepa']),
                       ('Ion Deposition', ['DUF-Ion'])])

class Record(LRecord, RecordDate, Record2Range):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    subexp = models.SmallIntegerField(choices=[(ind, k) for ind, k in enumerate(subexps.keys())], default=0)
    extraction = models.ForeignKey(Extraction, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_related",
                                   related_query_name="%(app_label)s_%(class)ss",
                                   )
    history = HistoricalRecords()

    def __str__(self):
        sub = self.submitted.strftime('%Y-%m-%d')
        try:
            return f'{activity_short} record {self.id} submitted the {sub}: {self.user} used '+\
                f'{self.experiment} the {self.date_from}: {self.get_time_from_display()} to {self.get_time_to_display()}'
        except:
            return 'Null record'


