from lending_site.models import Company,Vacancy


def get_queryset_company():
    company_queryset = Company.objects.filter(pk=1)
    name = company_queryset.name
    description = company_queryset.description
    image = company_queryset.image
    data = {
        name:'name',
        description:'description',
        image:'image'
    }
    return data

def get_queryset_vacancy():
    vacancy_queryset = Vacancy.objects.filter(activated=1)
    name = vacancy_queryset.name
    description = vacancy_queryset.description
    salary = vacancy_queryset.salary
    data = {
        name:'name',
        salary:'salary',
        description:'description',
        }
    return data
