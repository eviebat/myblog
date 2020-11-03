from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap

from . import views
from .feeds import LatestPostFeed

sitemaps = {'posts': PostSiteMap, }

app_name = 'blog'
urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]
