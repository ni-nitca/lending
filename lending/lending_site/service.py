from lending_site.models import (
    Company,
    Vacancy,
    Applicants,
    Contacts
    )


def get_queryset_company():
    company_queryset = Company.objects.get_or_create(pk=1)
    data = {
            'name':company_queryset[0].name,
            'description': company_queryset[0].description,
            'image': company_queryset[0].image,
        }
    return data

def get_queryset_vacancy():
    vacancy_queryset = Vacancy.objects.filter(activated=True).values()
    data = list(vacancy_queryset)
    return data

def get_contacts():
    contacts_queryset = Company.objects.get_or_create(pk=1)
    data = {
        'phone':contacts_queryset[0].phone,
        'email':contacts_queryset[0].email,
        'adress':contacts_queryset[0].adress
    }
    return data

def get_context(answer):
    company_data = get_queryset_company()
    vacancy_data = get_queryset_vacancy()
    contacts_data = get_contacts()
    data = {
        "company":company_data,
        "vacancy":vacancy_data,
        "answer":answer,
        "contacts":contacts_data
    }
    return data

def check_json(file_of_json):
    if file_of_json != []:
        values = file_of_json.keys()
        true_list = ["full_name","phone","email","comment","file"]
        if values == true_list:
            return True
        else:
            print('Неверно переданы ключи')
    else:
        print("Не передан словарь")


def save_applicants(file_of_json):
    if check_json(file_of_json) == True:
        applicants = Applicants
        applicants.full_name = file_of_json.full_name 
        applicants.phone = file_of_json.phone  
        applicants.email = file_of_json.email 
        applicants.comment = file_of_json.comment
        applicants.file = file_of_json.file
        applicants.save()


