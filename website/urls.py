from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<str:country>/', views.CountryPostsView.as_view(), name='country_posts'),
    path('<str:country>/<slug:slug>/', views.post_detail, name="post_detail"),
]