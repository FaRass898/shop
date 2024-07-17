from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product, Review
from product.serializers import ProductSerializer, ReviewSerializer, CategorySerializer


@api_view(http_method_names=['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def categories_detail_api_view(request):
    category = Category.objects.get(id=id)
    data = CategorySerializer(category, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_api_view(request):
    product = Product.objects.get(id=id)
    data = ProductSerializer(product, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_detail_api_view(request):
    review = Review.objects.get(id=id)
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)

