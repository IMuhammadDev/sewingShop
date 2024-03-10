from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/mahsulotlar/', views.MahsulotlarList.as_view()),
    path('api/mahsulotlar/<int:pk>/', views.MahsulotDetail.as_view()),
    path('api/xomashyolar/', views.XomashyolarList.as_view()),
    path('api/xomashyolar/<int:pk>/', views.XomashyoDetail.as_view()),
    path('api/omborxonalar/', views.OmborxonalarList.as_view()),
    path('api/omborxonalar/<int:pk>/', views.OmborxonaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
