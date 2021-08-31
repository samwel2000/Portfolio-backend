from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created', 'status')
    prepopulated_fields = {'slug':('title',),}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_setting','heading')
    
class ExperienceContentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'dates')

    
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ExperienceContent, ExperienceContentAdmin)
admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(HeroContent)
admin.site.register(AboutContent)
admin.site.register(Skill)
admin.site.register(ContactContent)

# admin site configurations
admin.site.site_header = "Samwel Godfrey Portfolio Backend"
admin.site.site_title = "Samwel Godfrey Portfolio Backend"
