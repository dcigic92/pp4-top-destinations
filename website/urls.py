from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_destination/', views.add_destination, name='add_destination'), 
    path('<str:country>/', views.CountryPostsView.as_view(), name='country_posts'),
    path('<str:country>/<slug:slug>/', views.post_detail, name="post_detail"),
    path('<str:country>/<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<str:country>/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]