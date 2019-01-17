from django.db import models

months = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec'.split(',')
weekdays = 'Mon,Tue,Wed,Thu,Fri,Sat,Sun'.split(',')

class Favourite(models.Model):
    fav_month = models.PositiveSmallIntegerField()
    fav_weekday = models.PositiveSmallIntegerField()

    def __str__(self):
        repr_format = 'Month: {}, Weekday: {}'
        try:
            if self.fav_month < 1 or self.fav_weekday < 1:
                raise IndexError()
            return repr_format.format(months[self.fav_month - 1], weekdays[self.fav_weekday - 1])
        except IndexError:
            # We shouldn't get here if questionnaire answer data is handled correctly
            return repr_format.format('??', '??')

