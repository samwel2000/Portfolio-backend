from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

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


class FilterPostList(ListAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        get_filter = self.kwargs['filter']
        print(get_filter)
        if get_filter.lower() == 'data analytics':
            filter_list = ['stata','R','MS excel']
        elif get_filter.lower() == 'web development':
            filter_list = ['HTML','CSS','Javascript','ReactJS','Django', 'Python']
        elif get_filter.lower() == 'statistical modelling':
            filter_list = ['statistics','R','stata']
        elif get_filter.lower() == 'mobile development':
            filter_list = ['Flutter','React Native']
        elif get_filter.lower() == 'software development':
            filter_list = ['HTML','CSS','Javascript','ReactJS','Django', 'Python','Flutter','React Native']
        else:
            filter_list = [get_filter]
        
        filter_list2 = []
        for filter_item in filter_list:
            for cat in Category.objects.all():
                if filter_item.lower() == cat.name.lower():
                    filter_list2.append(cat.id)
        print(filter_list,filter_list2)
        return Post.objects.filter(category__in=filter_list2)
    
    
class PostDetail(RetrieveAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


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
    
class CreateSubscriber(CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    
class ResumeView(ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer