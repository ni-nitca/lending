
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from lending_site.models import Company, Contacts, Applicants, Vacancy


class ContactsInline(admin.StackedInline):
    model = Contacts
    extra = 0

class CompanyAdmin(SingletonModelAdmin):
    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'image'
        ]

    inlines = [ContactsInline]


class ApplicantsInline(admin.StackedInline):
    model = Applicants
    extra = 0

class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
        fields = [
            'name',
            'description ',
            'salary',
            'create_date',
            'activated'
        ]
    inlines = [ApplicantsInline]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)