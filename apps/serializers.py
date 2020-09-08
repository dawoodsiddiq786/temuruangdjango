from apps.apis import User
from apps.models import Holiday
from common.serializers import CustomSerializer


class UserSerializer(CustomSerializer):
    class Meta:
        model = User
        fields = '__all__'


class HolidaySerializer(CustomSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'
