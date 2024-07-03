from django.shortcuts import render, redirect

from account.base import get_data


def about(request):
    data = get_data(request)
    return render(request, 'about/about.html', data)

