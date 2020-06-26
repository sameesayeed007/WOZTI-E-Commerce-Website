
from django.urls import path
from Payment_Application import views

app_name = "Payment_Application"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
]