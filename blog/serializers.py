from rest_framework import serializers
from .models import *
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','blog_intro','category','content','status','photo','slug')

        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class HeroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroContent
        fields = '__all__'
        
class AboutContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutContent
        fields = '__all__'
        
class ExperienceContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceContent
        fields = '__all__'
        
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        
class ContactContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactContent
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
        
        
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


