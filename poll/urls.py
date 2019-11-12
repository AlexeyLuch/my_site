from django.urls import path

from . import views
app_name = 'poll'


urlpatterns = [
	path('', views.all, name='all'),
	path('basicview', views.basic_one, name='basic_one'),
	path('chat/', views.chat, name='chat'),
	path('basicview/1', views.template_two, name='template_two'),
	path('support', views.support, name='support'),
	path('unique', views.unique, name='unique'),
	path('calculator', views.calculator, name='calculator'),
	path('script', views.order, name='order'),
    path('poll/', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
	path('articles/all/', views.articles, name='articles'),
	path('articles/get/<int:article_id>', views.article, name='article'),

]
