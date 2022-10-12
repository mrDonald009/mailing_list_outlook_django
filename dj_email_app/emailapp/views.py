from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings



def send_email_api(request):
    system = input('System that is not available: ')
    send_email_from_app(system=system)
    data = {
        'success': True,
        'message': 'api to send an email'
    }
    return JsonResponse(data)

def send_email_from_app(system):
    #subject_system_error = {f"Cбой системы - {system.upper()}."}
    #print(f'{subject_system_error.get(system)}')
    html_tpl_path = 'email_templates/index.html'
    context_data = {'system_name' : f'{system.upper()}'}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = 'saveliy_petrov_2011@mail.ru'
    email_msg = EmailMessage(f"Cбой системы - {system.upper()}.",
                             email_html_template, settings.APPLICATION_EMAIL,
                             [receiver_email],
                             reply_to=[settings.APPLICATION_EMAIL])
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)

