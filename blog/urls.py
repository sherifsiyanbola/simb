from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail'),
  url(r'^', views.BlogListView.as_view(), name = 'home'),
]