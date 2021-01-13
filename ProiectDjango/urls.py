from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.article_detail,
         name='post_detail'),
    path('<int:article_id>/share/',
         views.article_share, name='post_share'),
    path('supportEmail',views.SupportEmail_view, name = 'support')
]
