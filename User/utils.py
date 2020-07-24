import smtplib

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def check_addr(addr):
	return addr.street != "" and addr.street_number != None

'''
Using the smtplib to send an email to th admin with login info
'''
def email(nume, cart_obj, addr_obj, date):
	try:
	    server = smtplib.SMTP('smtp.gmail.com:587')
	    server.ehlo()
	    server.starttls()
	    server.login('radudjango@gmail.com', 'dovle2147')
	    message = """
	    Subject: Comanda \n\n
	    Hei! Ati primit o comanda:
	   	De la: {}
	   	Adresa: 
	   	Strada {} 
	   	Numar {}
	   	Bloc {} 
	   	Scara {} 
	   	Aparament {}
	   	Data de livrare {}
	    """.format(nume, addr_obj.street, addr_obj.street_number, addr_obj.bloc, addr_obj.scara, addr_obj.ap, date)
	    server.sendmail('radudjango@gmail.com', "andrei.crisan2147@gmail.com", message)
	    server.quit()
	except Exception as e:
	    raise ValidationError(
	            _('%(value)s \nerror sending the email'),
	            params={'value': str(e)},
	        )