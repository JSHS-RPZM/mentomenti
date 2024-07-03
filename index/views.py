import logging
import random

from django.shortcuts import render

from account.base import get_data

logger = logging.getLogger(__name__)

def index(request):
    data = get_data(request)

    return render(request, 'index/index.html', data)
