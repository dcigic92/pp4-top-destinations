from .models import Country, Post

def unique_countries(request):
    unique_countries = Country.objects.all()
    return {
        'unique_countries' : unique_countries
    }