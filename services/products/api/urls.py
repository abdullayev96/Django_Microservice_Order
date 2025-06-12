from django.urls import path, include
from django.contrib import admin
from . import views


from django.conf.urls.static import static
from django.conf import settings


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Product Microservice API",
        default_version='v1',
        description="My API description",
        terms_of_service="https://burhon96.pythonanywhere.com",
        contact=openapi.Contact(email="Tedbook@gmail.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
	path("private/categories/", views.CategoryListCreate.as_view()),
	path("products/list/", views.ProductListCreate.as_view()),
	path("products/delete/", views.ProductDelete.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)