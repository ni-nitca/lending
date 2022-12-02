from lending_site.models import (
    Company,
    Vacancy,
    Applicants
    )


def get_queryset_company():
    company_queryset = Company.objects.get_or_create(pk=1)
    data = {
            'name':company_queryset[0].name,
            'description': company_queryset[0].description,
            'image': company_queryset[0].image
        }
    return data

def get_queryset_vacancy():
    vacancy_queryset = Vacancy.objects.filter(activated=True).values()
    data = list(vacancy_queryset)
    if not data:
        vacancy_queryset = Vacancy.objects.get_or_create()
        vacancy_queryset = Vacancy.objects.filter(activated=True).values()
        data = list(vacancy_queryset)
        return data
    else:
        return data


def save_applicants(
    full_name,
    phone,
    email,
    comment,
    file
    ):
    applicants = Applicants
    applicants.full_name = full_name 
    applicants.phone = phone  
    applicants.email = email 
    applicants.comment = comment
    applicants.file = file
    applicants.save()


def get_context(answer):
    company_data = get_queryset_company()
    vacancy_data = get_queryset_vacancy()
    data = {
        "company":company_data,
        "vacancy":vacancy_data,
        "answer":answer
    }
    return data