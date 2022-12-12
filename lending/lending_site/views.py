from django.core.files.storage import FileSystemStorage

from django.shortcuts import (
    render,
)
from django.views.generic import (
    ListView,
)
from lending_site.service import (
    get_context,
    save_applicants,
)


class IndexListView(ListView):
    def get(self, request):
        template_name = 'lending_site/index.html'
        context = get_context()
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'lending_site/index.html'
        if request.method == 'POST' and request.FILES:
            data = request.POST
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
        
            saved = save_applicants(data,filename)
            context = get_context()
            context['saved'] = saved
            return render(request, template_name, context)
        else:
            data = request.POST
            filename = "No file"
            saved = save_applicants(data,filename)
            context = get_context()
            context['saved'] = saved
            return render(request, template_name, context)