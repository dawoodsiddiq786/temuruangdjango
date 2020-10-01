from rest_framework import serializers

from apps.apis import User
from apps.models import Activity, Image, Tour, Stay
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
    avg_rate = serializers.SerializerMethodField()
    all_rate = serializers.SerializerMethodField()
    total_rate = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else ""

    def get_supplier_image(self, obj):
        return obj.supplier.image if obj.supplier else None

    def get_image(self, obj):
        urls = []
        for image in obj.image.all():
            urls.append('https://demo.plugins360.com/wp-content/uploads/2017/12/demo.png')
            # urls.append(image.gallery.url)
        return urls

    def get_avg_rate(self, obj):
        return 2.5

    def get_total_rate(self, obj):
        return 2

    def get_all_rate(self, obj):
        return [
            {
                'rate': 5.0,
                'review': 'Good',
            },
            {
                'rate': 2.0,
                'review': 'not bad',
            }
        ]


class TourSerializer(CustomSerializer):
    image = serializers.SerializerMethodField()
    supplier_name = serializers.SerializerMethodField()
    supplier_image = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    all_rate = serializers.SerializerMethodField()
    total_rate = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = '__all__'


    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else ""

    def get_supplier_image(self, obj):
        return obj.supplier.image if obj.supplier else None


    def get_image(self, obj):
        urls = []
        for image in obj.image.all():
            urls.append('https://demo.plugins360.com/wp-content/uploads/2017/12/demo.png')
            # urls.append(image.gallery.url)
        return urls

    def get_avg_rate(self, obj):
        return 2.5

    def get_total_rate(self, obj):
        return 2

    def get_all_rate(self, obj):
        return [
            {
                'rate': 5.0,
                'review': 'ok',
            },
            {
                'rate': 2.0,
                'review': 'not fine',
            }
        ]


class StaySerializer(CustomSerializer):
    image = serializers.SerializerMethodField()
    supplier_name = serializers.SerializerMethodField()
    supplier_image = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    all_rate = serializers.SerializerMethodField()
    total_rate = serializers.SerializerMethodField()

    class Meta:
        model = Stay
        fields = '__all__'

    def get_avg_rate(self, obj):
        return 2.5

    def get_total_rate(self, obj):
        return 2

    def get_all_rate(self, obj):
        return [
            {
                'rate': 4.0,
                'review': 'Goosd',
            },
            {
                'rate': 3.0,
                'review': ' bad',
            }
        ]

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else ""

    def get_supplier_image(self, obj):
        return obj.supplier.image if obj.supplier else None


    def get_image(self, obj):
        urls = []
        for image in obj.image.all():
            urls.append('https://demo.plugins360.com/wp-content/uploads/2017/12/demo.png')
            # urls.append(image.gallery.url)
        return urls
