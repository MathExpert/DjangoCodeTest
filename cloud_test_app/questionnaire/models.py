from django.db import models

from questionnaire.utils import month_names, weekday_names

short_month_names = [m[:3] for m in month_names]
short_weekday_names = [d[:3] for d in weekday_names]

class Favourite(models.Model):
    fav_month = models.PositiveSmallIntegerField()
    fav_weekday = models.PositiveSmallIntegerField()

    def __str__(self):
        repr_format = 'Month: {}, Weekday: {}'
        try:
            if self.fav_month < 1 or self.fav_weekday < 1:
                raise IndexError()
            return repr_format.format(short_month_names[self.fav_month - 1],
                                      short_weekday_names[self.fav_weekday - 1])
        except IndexError:
            # We shouldn't get here if questionnaire answer data is handled correctly
            return repr_format.format('??', '??')

