from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.http import JsonResponse
from api.models.award import *


@csrf_exempt
def set_user_response(request):

    if request.method == "POST":

        with transaction.atomic():
            edition = Edition.objects.get(is_active=True)
            obj, created = UserNomination.objects.update_or_create(
                    category_id=request.POST.get("category"),
                    user=request.user, edition=edition,
                    defaults={'response': request.POST.get("response")}
                )

            if created:
                return JsonResponse({'message': 'Voto registrado com sucesso!'})
            return JsonResponse({'message': 'Voto alterado com sucesso!'})
    return JsonResponse({'message': 'fail'})