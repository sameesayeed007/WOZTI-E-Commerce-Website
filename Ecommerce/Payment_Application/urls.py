
from django.urls import path
from Payment_Application import views

app_name = "Payment_Application"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('pay/', views.payment, name="payment"),
    path('status/', views.complete, name="complete"),
    path('purchase/<val_id>/<tran_id>/', views.purchase, name="purchase"),
    path('orders/', views.order_view, name="orders"),
]