
from django.urls import path
from .views import UserView, JobView, login

urlpatterns = [
path('users/', UserView.as_view(), name='users-list'),
path('users//', UserView.as_view(), name='user-detail'),
path('jobs/', JobView.as_view(), name='jobs-list'),
path('jobs//', JobView.as_view(), name='job-detail'),
]

urlpatterns = [
    path('users/', UserView.as_view(), name='users-list'),
    path('users/<int:user_id>/', UserView.as_view(), name='user-detail'),
    path('jobs/', JobView.as_view(), name='jobs-list'),
    path('jobs/<int:job_id>/', JobView.as_view(), name='job-detail'),
    path('login/', login, name='login'),  # Маршрут для логина
]

