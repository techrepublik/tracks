import requests
from django.shortcuts import render

from django.http import request, HttpResponse

def get_profiles(request):
    url = 'https://trackz-api.herokuapp.com/profiles/'
    r = requests.get(url)
    # code = r['profile_code']
    # fullname = '{}, {} {}'.format(r['last_name'], r['first_name'], r['middle_name'])
    # resz = '{} {}'.format(code, fullname)
    return HttpResponse(r)

def get_profile(request, pk):
    url = 'https://trackz-api.herokuapp.com/profiles/{}/'
    r = requests.get(url.format(pk))
    # code = r['profile_code']
    # fullname = '{}, {} {}'.format(r['last_name'], r['first_name'], r['middle_name'])
    # resz = '{} {}'.format(code, fullname)
    return HttpResponse(r)
