from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/')
    created_at = models.DateTimeField(auto_now_add=True)
    button = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
    
    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    icon_class = models.CharField(max_length=50)
    details_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    
    def __str__(self):
        return self.client_name