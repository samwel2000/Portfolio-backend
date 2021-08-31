from django.urls import path
from  .views import *

app_name = 'blog_api'

urlpatterns = [
    path('posts-category/', PostCategories.as_view(), name="posCategories"),
    path('posts/', PostList.as_view(), name="postlist"),
    path('post/<str:pk>/', PostDetail.as_view(), name="postdetail"),
    path('hero-content/', HeroContentList.as_view(), name="heroContentlist"),
    path('about-content/', AboutContentList.as_view(), name="aboutContentlist"),
    path('experience-content/', ExperienceContentList.as_view(), name="experienceContentlist"),
    path('experience-organization/', OrganizationList.as_view(), name="OrganizationListlist"),
    path('skills-list/', SkillList.as_view(), name="skillslist"),
    path('contact-content/', ContactContentList.as_view(), name="contactContentlist"),
    path('projects-list/', ProjectstList.as_view(), name="projectslist"),
]
