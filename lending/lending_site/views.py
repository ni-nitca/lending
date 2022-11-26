from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )
from django.contrib import messages
from django.views.generic import (
    ListView,
    )

from lending_site.forms import ApplicantsForm
from lending_site.service import (
    get_queryset_company,
    get_queryset_vacancy,
    )


class IndexListView(ListView):
    form = ApplicantsForm
    template_name = 'lending_site/index.html'
    if request.method == 'GET':
        a = get_queryset_company
        b = get_queryset_vacancy

