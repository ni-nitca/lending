from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib import messages
from django.views.generic import (
    ListView,
)
from lending_site.models import (
    Company,
    Vacancy,
    Applicants,
)
from lending_site.forms import ApplicantsForm


class IndexListView(ListView):
    model1 = Company
    model2 = Vacancy
    form = ApplicantsForm
    template_name = 'lending_site/index.html'
    context = {}

    def get(self, request):
        self.context = {
            'company': self.model1.objects.all(),
            'vacancy': self.model2.objects.filter(activated=1)
        }
        return render(request, self.template_name, self.context, self.form)
