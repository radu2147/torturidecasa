from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def phone(value):
	if(len(value) != 10):
		raise ValidationError(
            _('%(value)s is not a phone number'),
            params={'value': value},
        )

def poz(value):
	if value < 0:
		raise ValidationError(
            _('%(value)s is not positive'),
            params={'value': value},
        )

def scara(value):
	if len(value) != 1 or value not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		raise ValidationError(
            _('%(value)s is not a phone number'),
            params={'value': value},
        )