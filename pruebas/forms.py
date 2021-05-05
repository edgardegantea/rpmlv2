from django.forms import *

from core.models import Temperatura


class TestForm(Form):

    date_ranger = CharField(
        queryset = Temperatura.objects.none(), widget=Select(
            attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }
        )
    )