from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from api.models.award import *


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/vote/")
    return render(request, "home.html", {})


@login_required(login_url='/')
def vote(request):
    edition = Edition.objects.get(is_active=True)
    categories = Category.objects.filter(edition=edition)
    responses = UserNomination.objects.filter(user=request.user, edition=edition)

    lista = []
    for category in categories:
        req = Requirement.objects.filter(category=category)
        obj = {'category': category, 'requirements': req}

        for r in responses:
            if category.id == r.category.id:
                obj['response'] = r.response 

        lista.append(obj)
    return render(request, "vote.html", {'lista': lista, 'responses': responses})