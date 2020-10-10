from django.db.models import Q
from rest_framework.exceptions import NotAcceptable

from apps.models import Activity, User, Stay, Tour, Place, Booking


def activity_filter(self, request):
    place = request.query_params.get('place')
    if place:
        return Activity.objects.filter(place_id=int(place))
    return Activity.objects.all()


def tour_filter(self, request):
    holiday_qs = Tour.objects.all()
    return holiday_qs


def place_filter(self, request):
    holiday_qs = Place.objects.all()
    return holiday_qs


def stay_filter(self, request):
    holiday_qs = Stay.objects.all()
    return holiday_qs


def booking_filter(self, request):
    id = request.query_params.get('id')
    user =User.objects.get(id=int(id))
    if user.is_user:
         holiday_qs = Booking.objects.filter(user_id=int(id))
    else:
        holiday_qs = Booking.objects.filter(Q(activity__supplier=user) |Q(tour__supplier=user) | Q(stay__supplier=user)  )

    return holiday_qs


def user_filter(self, request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')

    user_qs = User.objects.filter(email__exact=email, password__exact=password)
    if user_qs.exists():
        return user_qs
    raise NotAcceptable(detail='Wrong Credentials !')
