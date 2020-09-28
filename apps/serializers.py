from rest_framework import serializers

from apps.apis import User
from apps.models import Activity, Image
from common.serializers import CustomSerializer


class UserSerializer(CustomSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ImageSerializer(CustomSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ActivitySerializer(CustomSerializer):
    image = serializers.SerializerMethodField()
    supplier_name = serializers.SerializerMethodField()
    supplier_image = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get_supplier_name(self, obj):
        return obj.supplier.name

    def get_supplier_image(self, obj):
        return obj.supplier.name

    def get_image(self, obj):
        urls = []
        for image in obj.image.all():
            urls.append('https://demo.plugins360.com/wp-content/uploads/2017/12/demo.png')
            # urls.append(image.gallery.url)
        return urls
