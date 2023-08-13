from django.core.exceptions import ValidationError

def clean(value):
        if value == None:
            raise ValidationError('Campo nome é obrigatório!')