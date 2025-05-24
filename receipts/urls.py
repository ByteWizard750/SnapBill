from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.receipt_history, name='receipt_history'),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('receipt/<int:receipt_id>/mark-paid/', views.mark_paid, name='mark_paid'),
    path('receipt/<int:receipt_id>/delete/', views.delete_receipt, name='delete_receipt'),
    path('receipt/<int:receipt_id>/split/', views.split_bill, name='split_bill'),
    path('receipt/<int:receipt_id>/share/', views.generate_sharing_link, name='generate_sharing_link'),
    path('shared/<uuid:sharing_link>/', views.shared_receipt, name='shared_receipt'),
    path('signup/', views.signup, name='signup'),
] 