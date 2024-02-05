from django.views import View
from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.http import JsonResponse
from .forms import TemplateForm


class TemplView(View):
    def get(self, request):
        return render(request, 'app_landing/index.html')

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP
            all_data = {'name': form.cleaned_data.get("name"),
                        'email': form.cleaned_data.get("email"),
                        'message': form.cleaned_data.get("message"),
                        'ip': ip,
                        'user_agent': request.META.get('HTTP_USER_AGENT'),
                        }

            return JsonResponse(all_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

        return render(request, 'app_landing/index.html')


def app_landing_view(request):
    if request.method == "GET":
        return render(request, 'app_landing/index.html')

    if request.method == "POST":
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP
        all_data = {'name': request.POST.get("name"),
                    'email': request.POST.get("email"),
                    'message': request.POST.get("message"),
                    'ip': ip,
                    'user_agent': request.META.get('HTTP_USER_AGENT'),
                    }

        return JsonResponse(all_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})


