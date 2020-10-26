from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from Shop.settings import EMAIL_HOST_USER, EMAIL_ORDER_RECEIVER

def email(user, pers_obj):
    '''
    Function that sends personalized order data on email
    It raises an error when problems with sending email occur( login problems, internet connection )
    '''
    try:
        addr_obj = user.addr
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
        """.format(user.nume, user.email, addr_obj.street, addr_obj.street_number, addr_obj.bloc, addr_obj.scara, addr_obj.ap, pers_obj.image.url, pers_obj.description, pers_obj.quantity, pers_obj.date)
        send_mail("COMANDA {}".format(user.nume), message, EMAIL_HOST_USER, [EMAIL_ORDER_RECEIVER])
    except Exception as e:
        raise ValidationError(
                _('%(value)s \nerror sending the email'),
                params={'value': str(e)},
            )