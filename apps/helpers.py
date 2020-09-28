from rest_framework.exceptions import NotAcceptable

from apps.models import Activity, User


def activity_filter(self, request):
    holiday_qs = Activity.objects.all()
    return holiday_qs


def user_filter(self, request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')

    user_qs = User.objects.filter(email__exact=email, password__exact=password)
    if user_qs.exists():
        return user_qs
    raise NotAcceptable(detail='Wrong Credentials !')
