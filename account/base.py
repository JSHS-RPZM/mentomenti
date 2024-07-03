from django.contrib import auth

def get_data(request):
    data = {}

    user = auth.get_user(request)
    if user.is_authenticated:
        data['user'] = user
    else:
        pass

    return data
