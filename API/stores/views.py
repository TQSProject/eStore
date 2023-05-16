from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Store
from .serializers import StoreSerializer, ProductSerializer

class StoreList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context={"request": request})
        return Response(serializer.data)


class ProductList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data)

class StoreDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug):
        store = get_object_or_404(Store, slug=slug)
        serializer = StoreSerializer(store, context={"request": request})
        return Response(serializer.data)

class StoreProductListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug):
        products = Product.objects.filter(store__slug=slug)
        serializer = ProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data)

class StoreProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug, product_id):
        product = get_object_or_404(Product, id=product_id, store__slug=slug)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)

