from . import views
from django.urls import path

handler404 = "website.views.custom_404"

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('search/', views.SearchView.as_view(), name='search_posts'),
    path('<str:country>/', views.CountryPostsView.as_view(), name='country_posts'),
    path('<str:country>/<slug:slug>/', views.post_detail, name="post_detail"),
    path('<str:country>/<slug:slug>/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('<str:country>/<slug:slug>/delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('<str:country>/<slug:slug>/delete_post/<int:id>',
         views.delete_post, name='delete_post'),
    path('<str:country>/<slug:slug>/edit_post/<int:id>',
    views.edit_post, name='edit_post'),
]