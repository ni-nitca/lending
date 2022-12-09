from django.shortcuts import (
    render,
)
from django.views.generic import (
    ListView,
)
from lending_site.service import (
    get_context,
    save_applicants
)


class IndexListView(ListView):
    def get(self, request):
        template_name = 'lending_site/index.html'
        context = get_context()
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'lending_site/index.html'
        data = request.POST

        saved = save_applicants(data)
        context = get_context()
        context['saved'] = saved
        return render(request, template_name, context)
