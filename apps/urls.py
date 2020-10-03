from rest_framework import routers

from apps import apis

router = routers.DefaultRouter()

router.register('stay', apis.StayViewSet, basename='all_activity')
router.register('tour', apis.TourViewSet, basename='all_activity')
router.register('activity', apis.ActivityViewSet, basename='all_activity')
router.register('user', apis.UserViewSet, basename='all_holiday')
router.register('place', apis.PlaceViewSet, basename='all_place')

urlpatterns = [

]

urlpatterns += router.urls
