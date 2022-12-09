
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


class ApplicantsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'contact',
        'posted_date'
    )
    ordering = [
        'posted_date',
    ]

    class Meta:
        model = Applicants
        fields = [
            'contact',
            'full_name',
            'phone',
            'email',
            'comment',
            'posted_date',
            'file'
        ]


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary')

    class Meta:
        model = Vacancy
        fields = [
            'name',
            'description ',
            'salary',
            'create_date',
            'activated'
        ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Applicants, ApplicantsAdmin)
