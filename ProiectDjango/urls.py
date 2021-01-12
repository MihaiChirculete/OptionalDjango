from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.article_detail,
         name='post_detail'),
]
