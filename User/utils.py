from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def check_addr(addr):
    return addr.street != "" and addr.street_number != None

'''
Using the smtplib to send an email to th admin with login info
'''
def email(nume, addr_obj):
    try:
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
        """.format(nume, addr_obj.street, addr_obj.street_number, addr_obj.bloc, addr_obj.scara, addr_obj.ap)
        send_mail("COMANDA {}".format('nume'), message, 'radudjango@gmail.com', ["andrei.crisan2147@gmail.com"])
    except Exception as e:
        raise ValidationError(
                _('%(value)s \nerror sending the email'),
                params={'value': str(e)},
            )

def email_cart_products(nume, cart_obj, addr_obj):
    try:
        message = """Subject: Comanda \n\n
        Hei! Ati primit o comanda:
        De la: {}
        Adresa: 
        Strada {} 
        Numar {}
        Bloc {} 
        Scara {} 
        Aparament {}
        """.format(nume, addr_obj.street, addr_obj.street_number, addr_obj.bloc, addr_obj.scara, addr_obj.ap)
        message += '\nCART\n\n'
        print(len(cart_obj))
        for el in list(cart_obj):
            message += '''
            Nume: {}
            Inscriptie: {}
            Cantitate: {}
            Subpret: {}
            Data livrarii: {}
            '''.format(el.nume, el.inscr, el.gram, el.get_subtotal(), el.date_of_order)
        send_mail("COMANDA {}".format('nume'), message, 'radudjango@gmail.com', ["andrei.crisan2147@gmail.com"])
    except Exception as e:
        raise ValidationError(
                _('%(value)s \nerror sending the email'),
                params={'value': str(e)},
            )