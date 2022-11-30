from lending_site.models import (
    Company,
    Vacancy,
    )


def get_queryset_company():
    company_queryset = Company.objects.filter(pk=1)
    c_name = company_queryset.c_name
    description = company_queryset.description
    image = company_queryset.image
    data = {
        c_name:'name',
        description:'description',
        image:'image'
    }
    return data

def get_queryset_vacancy():
    vacancy_queryset = Vacancy.objects.filter(activated=1)
    v_name = vacancy_queryset.v_name
    pk = vacancy_queryset.id
    description = vacancy_queryset.description
    salary = vacancy_queryset.salary
    data = {
        v_name:'name',
        pk:'id',
        salary:'salary',
        description:'description',
        }
    return data

def get_context():
    company_data = get_queryset_company()
    vacancy_data = get_queryset_vacancy()
    data = [company_data,vacancy_data]
    return data