from lending_site.models import (
    Company,
    Vacancy,
    Applicants,
    Contacts
    )


def get_queryset_company():
    company_queryset = Company.objects.get_or_create(pk=1)[0]
    data = {
            'name':company_queryset.name,
            'description': company_queryset.description,
            'image': company_queryset.image,
        }
    return data

def get_queryset_vacancy():
    vacancy_queryset = Vacancy.objects.filter(activated=True).values()
    data = list(vacancy_queryset)
    return data

def get_contacts():
    contacts_queryset = Contacts.objects.filter(activated=True).values()
    data = list(contacts_queryset)
    return data

def check_json(file_of_json):
    if file_of_json != []:
        values = file_of_json.keys()
        true_list = ["full_name","phone","email","comment","file"]
        for value in true_list:
            if value not in values:
                return False
        return True
    else:
        print("Не передан словарь")

def save_applicants(file_of_json):
    if check_json(file_of_json):
        applicants = Applicants
        applicants.full_name = file_of_json['full_name'] 
        applicants.phone = file_of_json['phone']  
        applicants.email = file_of_json['email'] 
        applicants.comment = file_of_json['comment'] 
        applicants.file = file_of_json['file'] 
        applicants.save()
        return True
    else:
        return False

def get_context():
    company_data = get_queryset_company()
    vacancy_data = get_queryset_vacancy()
    contacts_data = get_contacts()
    data = {
        "company":company_data,
        "vacancy":vacancy_data,
        "contacts":contacts_data,
    }
    return data





