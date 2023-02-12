
from .models import Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Profile.objects.filter(name__icontains=search_query)
    # import Q use __icontains as arguments
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) 
    )

    return profiles, search_query


def paginateProfiles(request, profiles, results):
    # 'page' from html element
    page = request.GET.get('page')
    # paginator takes in profiles and results as arguments
    paginator = Paginator(profiles, results)

    try: 
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page) 
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    # EmptyPage will use num_pages attribute to send users to last page

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, profiles
    