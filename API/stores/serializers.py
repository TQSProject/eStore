from rest_framework import serializers
from .models import Store, Product, ProductTag


class StoreSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    store = serializers.StringRelatedField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)