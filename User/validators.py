from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def phone(value):
	if len(value) != 10 or value.startswith("0") == False or len([x for x in list(value) if x not in "0123456789"]) > 0:
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

def valid_pass(value):
	return len(value) > 7

def valid_name(value):
	return len(value) > 0