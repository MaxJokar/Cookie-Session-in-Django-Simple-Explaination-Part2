from django.urls import path
import apps.cookiestest.views as views



urlpatterns = [
    path('',views.index),
    path('set/',views.set_cookies),
    path('get/',views.get_cookies),
    
    
]
