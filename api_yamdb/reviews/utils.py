from datetime import date

from rest_framework.exceptions import ValidationError


def validate_date(value):
    current_year = int(date.today().year)
    if value > current_year or value <= 0:
        raise ValidationError('Wrong date!')
