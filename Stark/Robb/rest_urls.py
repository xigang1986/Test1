
from django.conf.urls import url,include
from  Robb import views

urlpatterns = [
    url(r'client/config/(\d+)/$',views.client_configs ),
    url(r'client/service/report/$',views.service_data_report ),

]
