# Create your views here.

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .models import Job, News
from .serializers import JobSerializer, NewsSerializer
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import User, Job
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Класс представления для пользователей
class UserView(View):
    def get(self, request, user_id=None):
        if user_id:
            user = get_object_or_404(User, id=user_id)
            response = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        else:
            users = User.objects.all()
            response = [{'id': user.id, 'username': user.username} for user in users]
        return JsonResponse(response, safe=False)

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        return JsonResponse({'id': user.id, 'username': user.username})

# Класс представления для вакансий
class JobView(View):
    def get(self, request, job_id=None):
        if job_id:
            job = get_object_or_404(Job, id=job_id)
            response = {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'company': job.company,
                'location': job.location,
                'salary': job.salary,
            }
        else:
            jobs = Job.objects.all()
            response = [{'id': job.id, 'title': job.title, 'company': job.company} for job in jobs]
        return JsonResponse(response, safe=False)

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        job = Job.objects.create(
            title=data['title'],
            description=data['description'],
            company=data['company'],
            location=data['location'],
            salary=data['salary'],
            posted_by=User.objects.get(id=data['posted_by']),
        )
        return JsonResponse({'id': job.id, 'title': job.title})


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

def home(request):
       return HttpResponse("Welcome to Job Platform")


