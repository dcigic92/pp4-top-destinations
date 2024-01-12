from .models import Country, Post

def unique_countries(request):
    unique_countries = []
    # get all posts
    posts = Post.objects.all()
    # get all unique countries that are used in posts
    for post in posts:
        # get country object from post
        country = Country.objects.get(id=post.country_of_destination.id)
        # check if country is already in list
        if country not in unique_countries:
            unique_countries.append(country)
    # sort by names
    unique_countries.sort(key=lambda x: x.name)

    # return list of unique countries
    return {
        'unique_countries' : unique_countries
    }