from django.urls import path
from . import views




urlpatterns = [
	path("emails/send/", views.email_send)
]



