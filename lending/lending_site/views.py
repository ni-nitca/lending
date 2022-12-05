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
        template_name = 'lending_site/index.html'
        alplicants_answer = False
        context = get_context(alplicants_answer)
        return render(request, template_name, context)

    def post(self, request):
        applicants_answer = True
        template_name = 'lending_site/index.html'
        saved = save_applicants(file_of_json)
        context = get_context(applicants_answer,saved) 
        return render(request,template_name,context)


