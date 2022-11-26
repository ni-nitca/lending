from lending_site.models import Company,Vacancy


def get_queryset_company():
    company = Company
    company_queryset = company.objects.all()
    return company_queryset


def get_queryset_vacancy():
    vacancy = Vacancy
    vacancy_queryset = vacancy.objects.filter(activated=1)
    return vacancy_queryset
