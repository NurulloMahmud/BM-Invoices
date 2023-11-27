from django.urls import path
from brokers.views import BrokerCreateView, BrokerListView


app_name = "brokers"
urlpatterns = [
    path('create/', BrokerCreateView.as_view(), name='create-broker'),
    path('all/', BrokerListView.as_view(), name='brokers-list')
]