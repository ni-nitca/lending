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
    def get(self, request):
        template_name = 'lending_site/index.html'
        context = get_context()
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'lending_site/index.html'
        data = request.data
        saved = save_applicants(data)
        save_dict = {"saved":saved}
        context = get_context() + save_dict
        return render(request,template_name,context)


