from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Store
from .serializers import StoreSerializer, ProductSerializer

from django.db.models import Q


class StoreList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        search_query = request.GET.get('q', None)

        stores = Store.objects.all()

        # Filter queryset based on name or type
        if search_query:
            stores = stores.filter(
                Q(name__icontains=search_query) | Q(type__icontains=search_query)
            )

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
