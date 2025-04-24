from django.contrib import admin
from .models import Category, PortfolioItem, Client, Service, Testimonial

admin.site.register(Category)
admin.site.register(PortfolioItem)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Testimonial)