from django.db.models import Q
from rest_framework.exceptions import NotAcceptable

from apps.models import Holiday, User


def holiday_filter(self, request):
    param_date = request.query_params.get('date')

    # date = dateutil.parser.parse(param_date)
    # offer_qf = Q()
    # if is_featured:
    #     offer_qf &= Q(is_featured=bool(is_featured))
    # if status:
    #     offer_qf &= Q(status=int(status))

    holiday_qs = Holiday.objects.all()

    return holiday_qs


def user_filter(self, request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')
    user_qf = Q()
    if email and password:
        user_qf &= Q(email__exact=email, password__exact=password)

    else:
        return User.objects.all()
    # if status:
    #     offer_qf &= Q(status=int(status))

    user_qs = User.objects.filter(user_qf)
    if user_qs.count()<1:
        raise NotAcceptable(detail='Wrong Credentials !')
    return user_qs
