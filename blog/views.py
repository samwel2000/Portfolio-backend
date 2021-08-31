from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *

class ProjectstList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    

class PostCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class PostList(ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    
class PostDetail(RetrieveAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class HeroContentList(ListAPIView):
    queryset = HeroContent.objects.all()
    serializer_class = HeroContentSerializer


class AboutContentList(ListAPIView):
    queryset = AboutContent.objects.all()
    serializer_class = AboutContentSerializer


class ExperienceContentList(ListAPIView):
    queryset = ExperienceContent.objects.all()
    serializer_class = ExperienceContentSerializer


class OrganizationList(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class SkillList(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ContactContentList(ListAPIView):
    queryset = ContactContent.objects.all()
    serializer_class = ContactContentSerializer