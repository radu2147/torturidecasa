from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

def date_check(date):
	l=str(date).split("-")
	now = str(timezone.now()).split(" ")[0].split("-")
	return l[0] > now[0] or l[1] > now[1] or l[2] > now[2]

def valid_date(date):
	if not date_check(date):
		raise ValidationError(
            _('%(value)s nu e o data valida'),
            params={'value': date},
        ) 