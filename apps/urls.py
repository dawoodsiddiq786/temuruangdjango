from rest_framework import routers

from apps import apis

router = routers.DefaultRouter()

# router.register('holiday', apis.HolidayViewSet, basename='all_holiday')
router.register('user', apis.UserViewSet, basename='all_holiday')

urlpatterns = [

]

urlpatterns += router.urls
