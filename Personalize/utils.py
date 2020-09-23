from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def email(user, pers_obj, addr_obj):
	try:
	    message = """
	    Subject: Comanda personalizata\n\n
	    Hei! Ati primit o comanda:
	   	De la: {}
	   	Email: {}
	   	Adresa: 
	   	Strada {} 
	   	Numar {}
	   	Bloc {} 
	   	Scara {} 
	   	Aparament {}

	   	Continut:
	   	Imagine {}
	   	Descriere {}
	   	Cantitate {}
	   	Data de livrare {}
	    """.format(user.nume, user.email, addr_obj.street, addr_obj.street_number, addr_obj.bloc, addr_obj.scara, addr_obj.ap, pers_obj.tort, pers_obj.description, pers_obj.quantity, pers_obj.date)
	    send_mail("COMANDA {}".format('nume'), message, 'radudjango@gmail.com', ["andrei.crisan2147@gmail.com"])
	except Exception as e:
	    raise ValidationError(
	            _('%(value)s \nerror sending the email'),
	            params={'value': str(e)},
	        )