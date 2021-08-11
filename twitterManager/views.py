
# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
# import oauth2 as oauth
# import requests

# CONSUMER_KEY = "mXAtQH6u0iQgEvaJC6ilxLqP0"
# CONSUMER_SECRET = "ngANEzIGDX07GBg6qmx0eCRED3bc7JyjczHkGNNrHBCvQDXyPL"
# consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)


@login_required
def top_page(request):

    user = UserSocialAuth.objects.get(user_id=request.user.id)
    pageDic = {
        'hoge': 'fuga',
        'user': user
    }
    # print("user.access_token", user.access_token)

    # token = oauth.Token(user.access_token["oauth_token"],
    #                     user.access_token["oauth_token_secret"])
    # print("token:", token)
    # client = oauth.Client(consumer, token)
    # print("client:", client)
    # url = "https://api.twitter.com/2/users?ids="+user.access_token["user_id"]
    # response = requests.get(url=url)
    # print(response.json())

    try:
        twitter_login = request.user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        line_login = request.user.social_auth.get(provider='line')
    except UserSocialAuth.DoesNotExist:
        line_login = None

    logindict = {
        'twitter_login': twitter_login,
        'line_login': line_login
    }
    pageDic.update(logindict)
    return render(request, 'top/index.html', pageDic)
