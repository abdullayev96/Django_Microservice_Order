from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import HasAuthIDPermission


class CategoryListCreate(APIView):
    permission_classes = [HasAuthIDPermission]

    def get(self, request):
        cats = Category.objects.all()
        srlz = CategorySerializer(cats, many=True)
        return Response(srlz.data)

    def post(self, request):
        name = request.data.get("category_name")
        if name:
            Category.objects.create(name=name)
            return Response({"message": "Category created"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)



class ProductListCreate(APIView):
    def get(self, request):
        cat_id = request.query_params.get("cat_id")
        prod_id = request.query_params.get("prod_id")
        if cat_id:
            products = Product.objects.filter(category_id=cat_id)
        elif prod_id:
            products = Product.objects.filter(id=prod_id)
        else:
            products = Product.objects.all()

        if products.exists():
            srlz = ProductSerializer(products, many=True)
            return Response(srlz.data)
        return Response({"message": "Sorry not found!"}, status=404)

    def post(self, request):
        data = request.data
        try:
            product = Product.objects.create(
                category_id=data["cat_id"],
                name=data["prod_name"],
                price=data["prod_price"],
                description=data["prod_description"]
            )
            return Response({"message": "Product added successfully"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)



class ProductDelete(APIView):
    def delete(self, request):
        prod_id = request.data.get("prod_id")
        if not prod_id:
            return Response({"message": "Product ID required"}, status=400)
        try:
            product = Product.objects.get(id=prod_id)
            product.delete()
            return Response({"message": "Product deleted successfully"}, status=204)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=404)





# from rest_framework.views import APIView
# from .models import Category, Product
# import json
# from rest_framework.response import Response
# from .serializers import CategorySerializer, ProductSerializer
# from rest_framework.decorators import api_view
#
#
#
# @api_view(http_method_names=["GET", "POST"])
# def categories(request):
# 	if not request.META["HTTP_AUTH_ID"] or request.META["HTTP_AUTH_ID"] != "MY155":
# 		return Response({"message": "Authorization Failed"})
#
# 	if request.method == "POST":
# 		new_cat = Category.objects.create(name=request.data["category_name"])
# 	categories_lst = Category.objects.all()
# 	srlz = CategorySerializer(categories_lst, many=True)
# 	return Response(srlz.data)
#
#
# @api_view(http_method_names=["GET"])
# def products_fetch(request):
# 	if request.query_params.get("cat_id"):
# 		products_list = Product.objects.filter(category__id=request.query_params.get("cat_id"))
# 	elif request.query_params.get("prod_id"):
# 		products_list = Product.objects.filter(id=request.query_params.get("prod_id"))
# 	else:
# 		products_list = Product.objects.all()
# 	if products_list:
# 		srlz = ProductSerializer(products_list, many=True)
# 		return Response(srlz.data, status=200)
# 	else:
# 		return Response({"message": "Sorry not found!"}, status=404)
#
#
# @api_view(http_method_names=["POST"])
# def products_create(request):
# 	new_prod = Product.objects.create(
# 		category=request.data["cat_id"],
# 		name=request.data["prod_name"],
# 		price=request.data["prod_price"],
# 		description=request.data["prod_description"],
# 	)
# 	return Response({"message": "Product added successfully"}, status=300)
#
#
#
# @api_view(http_method_names=["DELETE"])
# def products_delete(request):
# 	if not request.data["prod_id"]:
# 		return Response({"message": "Sorry not found!"}, status=500)
# 	product = Product.objects.get(id=request.data["prod_id"])
# 	product.delete()
# 	return Response({"message": "Product deleted successfully"}, status=300)
