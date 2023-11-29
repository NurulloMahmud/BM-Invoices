from django.urls import path
from invoices.views import (
    InvoiceListView, InvoiceCreateView, InvoiceStatusChangeView, InvoiceCommentView
    )


app_name = "invoices"
urlpatterns = [
    path('all/', InvoiceListView.as_view(), name='invoices-list'),
    path('create/', InvoiceCreateView.as_view(), name='create-invoice'),
    path('edit/<int:pk>/<str:status>/', InvoiceStatusChangeView.as_view(), name='edit-status'),
    path('comment/<int:pk>/', InvoiceCommentView.as_view(), name='comment'),
]