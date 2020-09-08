from rest_framework.permissions import AllowAny

from apps import helpers
from apps.models import Holiday, User
from apps.serializers import HolidaySerializer, UserSerializer
from common.apis import FullViewSet


class UserViewSet(FullViewSet):
    permission_classes = (AllowAny,)
    ObjModel = User
    ObjSerializer = UserSerializer

    def obj_filter(self, request):
        return helpers.user_filter(self, request)


class HolidayViewSet(FullViewSet):
    permission_classes = (AllowAny,)
    ObjModel = Holiday
    ObjSerializer = HolidaySerializer

    def obj_filter(self, request):
        return helpers.holiday_filter(self, request)
