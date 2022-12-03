from django.shortcuts import (
    HttpResponse,
    render,
    )
from django.views.generic import (
    ListView,
    )
from lending_site.service import (
    get_context,
    save_applicants

    )
from lending_site.models import Applicants



class IndexListView(ListView):
    def get(self, request ):
        template_name = 'lending/index.html'
        alplicants_answer = False
        context = get_context(alplicants_answer)
        return render(request, template_name, context)

    def post(self, request):
        applicants_answer = True
        template_name = 'lending/index.html'
        context = get_context(applicants_answer) 
        save_applicants(file_of_json)

        return render(request,template_name,context)


