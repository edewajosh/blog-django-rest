from django.urls import path

from .views import ArticleView, SingleArticleView

app_name = 'articles'

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>/', ArticleView.as_view()),
    path('article/<int:pk>/', SingleArticleView.as_view()),
]
