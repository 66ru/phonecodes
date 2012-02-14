import re
from django.db import models
from utils.exceptions import WrongNumberException, OperatorNotFoundException


class Operator(models.Model):
    name = models.CharField(max_length=250)
    region_code = models.PositiveIntegerField()
    number_start_range = models.PositiveIntegerField()
    number_end_range = models.PositiveIntegerField()
    mobile = models.BooleanField()
    region = models.CharField(max_length=250)

    class Meta:
        ordering = ['region_code', 'number_end_range']

    @staticmethod
    def _get_cleaned_number(number):
        cleaned = re.sub(r'\D', r'', number)
        if len(cleaned) != 11:
            raise WrongNumberException
        return cleaned

    @classmethod
    def find(cls, phone):
        cleaned = cls._get_cleaned_number(phone)
        region_code = cleaned[1:4]
        number = cleaned[4:]
        region_operators = cls.objects.filter(region_code=int(region_code))
        try:
            operator = region_operators.filter(number_end_range__gte=int(number))[0]
        except IndexError:
            raise OperatorNotFoundException
        return operator