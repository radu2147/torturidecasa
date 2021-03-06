from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from Shop.settings import EMAIL_HOST_USER, EMAIL_ORDER_RECEIVER

def check_addr(addr):
    '''
    Checks the validity of the address
    '''
    return addr.street != "" and addr.street_number != None

def email_cart_products(user, cart_obj):
    '''
    Sends the products from cart_page on email
    '''
    try:
        addr_obj = user.addr
        message = """Subject: Comanda \n\n
        Hei! Ati primit o comanda:
        De la: {}
        Email: {}
        Adresa: 
        Strada {} 
        Numar {}
        Bloc {} 
        Scara {} 
        Aparament {}
        """.format(user.nume, user.email, addr_obj.street, addr_obj.street_number, addr_obj.bloc, addr_obj.scara, addr_obj.ap)
        message += '\nCART\n\n'
        for el in list(cart_obj):
            message += '''
            Nume: {}
            Inscriptie: {}
            Cantitate: {}
            Subpret: {}
            Data livrarii: {}
            '''.format(el.nume, el.inscr, el.gram, el.get_subtotal(), el.date_of_order)
        send_mail("COMANDA {}".format(user.nume), message, EMAIL_HOST_USER, [EMAIL_ORDER_RECEIVER])
    except Exception as e:
        raise ValidationError(
                _('%(value)s \nerror sending the email'),
                params={'value': str(e)},
            )