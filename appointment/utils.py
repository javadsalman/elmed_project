from django.conf import settings
import requests

def check_recatpcha(request_data):
    return requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': request_data
    }).json()