#from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from api.models.award import *

from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User


class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        try:
            user = User.objects.get(email=sociallogin.account.extra_data['email'])
            perform_login(request, user, email_verification='optional')
            raise ImmediateHttpResponse(redirect(settings.LOGIN_REDIRECT_URL))
        except User.DoesNotExist:
            pass


def set_user_response(request):

    if request.method == "POST":
        try:
            with transaction.atomic():
                edition = Edition.objects.get(is_active=True)
                category = Category.objects.get(id=request.POST.get("category"), edition=edition)
                obj, created = UserNomination.objects.update_or_create(
                        category=category, user=request.user, edition=edition,
                        defaults={'response': request.POST.get("response")}
                    )

                if created:
                    return JsonResponse({'message': 'Voto registrado com sucesso!'}, status=200)
                return JsonResponse({'message': 'Voto alterado com sucesso!'}, status=200)
        except:
            return JsonResponse({'message': 'Desculpe, ocorreu algum erro!'}, status=500)
    return JsonResponse({'message': 'Método não autorizado'}, status=500)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')