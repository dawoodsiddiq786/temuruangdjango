from rest_framework.permissions import AllowAny

from apps import helpers
from apps.models import Activity, User
from apps.serializers import ActivitySerializer, UserSerializer
from common.apis import FullViewSet


class UserViewSet(FullViewSet):
    """
    create:
         User Signup
         ---

         Sample Signup Data:
         ---
                {
                  'name': 'Tas',
                  'company': '',
                  'phone': '',
                  'password': '1234rtyu',
                  'email': 'test@gmail.com',
                 }

    list:
        User Login
        ---

        Sample Login Data:
            ---
                Query parameters:
                ---
                    email:
                        type: string
                        required: yes
                    password:
                        type: string
                        required: yes

         Successful Login Response:
            ---
                  [
                      {
                        'last_login': None,
                        'is_staff': False,
                        'name': 'Tas',
                        'company': '',
                        'date_joined': '2020-09-08T21:36:52.133452Z',
                        'device_id': '',
                        'phone': '',
                        'password': '1234rtyu',
                        'is_user': True,
                        'image': 'https://hueys-list.s3-ap-southeast-2.amazonaws.com/ScBKUMNEguunnamed.png',
                        'is_superuser': False,
                        'email': 'test@gmail.com',
                        'is_active': True,
                        'id': 1,
                        'is_vendor': False,
                        'fb_id': ''
                      }
                    ]


        """

    permission_classes = (AllowAny,)
    ObjModel = User
    ObjSerializer = UserSerializer

    def obj_filter(self, request):
        return helpers.user_filter(self, request)


class ActivityViewSet(FullViewSet):
    permission_classes = (AllowAny,)
    ObjModel = Activity
    ObjSerializer = ActivitySerializer

    def obj_filter(self, request):
        return helpers.activity_filter(self, request)
