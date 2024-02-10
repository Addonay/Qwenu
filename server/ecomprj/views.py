from django.http import JsonResponse
from .serializers import ProductSerializer, CategorySerializer, RatingSerializer, UserSerializer
from products.models import Product
from category.models import Category
from reviews.models import Rating
from oauth.models import User

# Create your views here.
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({"users":serializer.data}, safe=False)
    elif request.method == "POST":
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({"products":serializer.data}, safe=False)
    elif request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({"categories":serializer.data}, safe=False)
    elif request.method == "POST":
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def rating_list(request):
    if request.method == "GET":
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return JsonResponse({"ratings":serializer.data}, safe=False)
    elif request.method == "POST":
        data = request.data
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)