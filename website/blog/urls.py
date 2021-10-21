from django.urls import path
from .views import homeView, detailView
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', homeView, name = 'home'),
    path('<int:post_id>/', detailView, name = 'detail'),

]

