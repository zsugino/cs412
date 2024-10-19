
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
  path('', views.RandomArticleView.as_view(), name='random'),
  path('show_all', views.ShowAllView.as_view(), name='show_all'),
  path('article/<int:pk>', views.ArticleView.as_view(), name='article'),
  # path('create_comment', views.CreateCommentView.as_view(), name='create_comment')
  path('article/<int:pk>/create_comment', views.CreateCommentView.as_view(), name='create_comment'), ### NEW
  path('create_article', views.CreateArticleView.as_view(), name='create_article'),
]

