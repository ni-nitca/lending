from django.shortcuts import (
    HttpResponse,
    render,
    )
from django.contrib import messages
from django.views.generic import (
    ListView,
    )
from lending_site.service import (
    get_queryset_company,
    get_queryset_vacancy,
    )
from lending_site.models import Applicants



class IndexListView(ListView):
    def get(self, request ):
        template_name = 'lending/index.html'
        company_data = get_queryset_company
        vacancy_data = get_queryset_vacancy
        return render(request, template_name,vacancy_data,company_data)
    
    def post(self, request):
        applicants = Applicants
        full_name = applicants.full_name
        phone = applicants.phone 
        email = applicants.email
        comment = applicants.comment
        file = applicants.file
        return HttpResponse('Ваше резюме отправлено,с вами свяжутся в ближайшее время')


