from django.urls import path
from invoices.views import (
    InvoiceListView, InvoiceCreateView, InvoiceStatusChangeView, InvoiceCommentView,
    InvoiceDetailView, GetBrokerForInvoice,
    )


app_name = "invoices"
urlpatterns = [
    path('all/', InvoiceListView.as_view(), name='invoices-list'),
    path('create/', InvoiceCreateView.as_view(), name='create-invoice'),
    path('edit/<int:pk>/<str:status>/', InvoiceStatusChangeView.as_view(), name='edit-status'),
    path('comment/<int:pk>/', InvoiceCommentView.as_view(), name='comment'),
    path('invoice-detail/<int:pk>', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('get-broker-for-invoice/', GetBrokerForInvoice.as_view(), name='get-broker-for-invoice'),
]