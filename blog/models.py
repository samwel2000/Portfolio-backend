from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name.capitalize()
    
    class Meta:
        verbose_name_plural = "Blog Categories"
        
    
class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
    
    STATUS_CHOICES = [
        ('draft','DRAFT'),
        ('published','PUBLISHED'),
    ]
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to="blog", default="default.png")
    blog_intro = models.TextField()
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='published')
    
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ('-created',)
        
class Project(models.Model):
    photo = models.ImageField(upload_to='project', null=True, blank=True)
    project_setting = models.CharField(max_length=300, default="featured project")
    heading = models.CharField(max_length=200)
    content = models.TextField()
    project_stack = models.TextField(help_text="Enter stack separated by a cooma")
    project_link =models.CharField(max_length=1000, null=True, blank=True)
    github_link =models.CharField(max_length=1000, null=True, blank=True)
    playstore_link =models.CharField(max_length=1000, null=True, blank=True)
    appstore_link =models.CharField(max_length=1000, null=True, blank=True)
    made_at =models.CharField(max_length=1000, default=".......")
    year =models.IntegerField(default=2021)
    
    def __str__(self):
        return self.heading

    class Meta:
        ordering = ('-year',)
    
class HeroContent(models.Model):
    bio_header = models.CharField(max_length=1000)
    bio_content = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Hero Content'
        
class AboutContent(models.Model):
    section1 = models.TextField()
    section2 = models.TextField()
    section3 = models.TextField()
    photo = models.ImageField(upload_to='about')
    
    class Meta:
        verbose_name_plural = 'About Content'
    
class Organization(models.Model):
    organization = models.CharField(max_length=1000)
    abbreviation = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.organization[:100]
    
    class Meta:
        verbose_name_plural = 'Exp Organizations'
    
class ExperienceContent(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    dates = models.CharField(max_length=100)
    duties = models.TextField(help_text="Enter duties separated by a cooma")
    
    class Meta:
        verbose_name_plural = 'Experience Content'
        
class Skill(models.Model):
    heading = models.CharField(max_length=1000)
    skill_liist = models.TextField(help_text="Enter skills separated by a comma")
    
    def __str__(self):
        return self.heading
    
class ContactContent(models.Model):
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contact Content'
        
class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email

class Resume(models.Model):
    file = models.FileField(upload_to='resume', max_length=300, storage=RawMediaCloudinaryStorage())
    
    def __str__(self):
        return "My resume"
    
    class Meta:
        verbose_name_plural = 'Resume'