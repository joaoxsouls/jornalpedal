from django.conf import settings


def site(request):
    return {'CURRENT_URL': settings.SITE_URL + request.path}
