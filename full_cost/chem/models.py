from pathlib import Path
from full_cost.utils.constants import ACTIVITIES
from django.db import models
from lab.models import Record as LRecord
from lab.models import Extraction
from lab.models import Record2Range, RecordDate, Record4Range
from simple_history.models import HistoricalRecords

activity_short = Path(__file__).parts[-2]

sub_billings = ACTIVITIES[activity_short]['sub_billings']



class Experiment(models.Model):
    experiment = models.CharField(max_length=200)
    exp_type = models.CharField(choices=sub_billings, default=sub_billings[0][0], max_length=200)
    def __str__(self):
        return '{:s}'.format(self.experiment)

# class Extraction(Extraction):
#     history = HistoricalRecords()

class Record(LRecord, RecordDate, Record4Range):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    extraction = models.ForeignKey(Extraction, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_related",
                                   related_query_name="%(app_label)s_%(class)ss",
                                   )
    history = HistoricalRecords()

    def __str__(self):
        sub = self.submitted.strftime('%Y-%m-%d')
        try:
            return f'{activity_short} record {self.id} submitted the {sub}: {self.user} used '+\
                f'{self.experiment} from {self.date_from}/{self.get_time_from_display()} to {self.date_to}/{self.get_time_to_display()}'
        except:
            return 'Null record'


