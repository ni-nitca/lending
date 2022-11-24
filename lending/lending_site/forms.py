from django import forms
from lending_site.models import Applicants


class ApplicantsForm(forms.ModelForm):
    class Meta:
        model = Applicants
        fields = (
            'full_name',
            'phone',
            'email',
            'comment',
            #выбор вакансии
        )