from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request,'index.html')


from .models import PortfolioItem, Category, Client, Service, Testimonial

def index(request):
    portfolio_items = PortfolioItem.objects.select_related('category').all()
    categories = Category.objects.distinct()
    clients = Client.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'portfolio_items': portfolio_items,
        'categories': categories,
        'clients': clients,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)