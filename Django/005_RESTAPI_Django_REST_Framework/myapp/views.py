from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer
