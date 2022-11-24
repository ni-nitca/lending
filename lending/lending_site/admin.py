from django.contrib import admin

from lending_site.models import Company, Contacts, Applicants, Vacancy


class ContactsInline(admin.StackedInline):
    model = Contacts
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

admin.site.register(Applicants, ApplicantsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)