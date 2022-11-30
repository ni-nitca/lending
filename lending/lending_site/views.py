from django.shortcuts import (
    HttpResponse,
    render,
    )
from django.views.generic import (
    ListView,
    )
from lending_site.service import (
    get_context,

    )
from lending_site.models import Applicants



class IndexListView(ListView):
    def get(self, request ):
        template_name = 'lending/index.html'
        context = get_context()
        return render(request, template_name, context)
    def post(self, request):
        template_name = 'lending/index.html'
        status_code = ['1']
        context = get_context() + status_code
        applicants = Applicants
        full_name = applicants.full_name
        phone = applicants.phone 
        email = applicants.email
        comment = applicants.comment
        file = applicants.file
        applicants.save()
        return render(request,template_name,context)


