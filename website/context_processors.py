from .models import Country

def unique_countries(request):
    unique_countries = Country.objects.all()
    return {
        'unique_countries' : unique_countries
    }