from django.contrib import admin

from lending_site.models import Company, Contacts, Applicants, Vacancy


class ContactsInline(admin.StackedInline):
    model = Company
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'image'
        ]

    inlines = [ContactsInline]

class VacancyInline(admin.StackedInline):
    model = Vacancy
    extra = 0

class ApplicantsAdmin(admin.ModelAdmin):
    class Meta:
        model = Applicants
        fields = [
            'full_name',
            'phone ',
            'email',
            'comment',
            'posted_date'
        ]

    inlines = [VacancyInline]

admin.site.register(Company, CompanyAdmin, Applicants, ApplicantsAdmin)