from lending_site.models import (
    Company,
    Vacancy,
    Applicants,
    Contacts
)
from django.core.files.storage import FileSystemStorage



def get_queryset_company():
    company_queryset = Company.objects.get_or_create(pk=1)[0]
    data = {
        'name': company_queryset.name,
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
        true_list = [
            "full_name",
            "phone",
            "email",
            "comment",
        ]
        for value in true_list:
            if value not in values:
                return False
        return True
    else:
        return False



def save_applicants(req):
    fs = FileSystemStorage()
    if req.method == 'POST' and req.FILES:
        data = req.POST
        file = req.FILES['file']
        filename = fs.save(file.name, file)
        return save(data,filename)

    else:
        data = req.POST
        filename = "No file"
        return save(data,filename)


def save(data,file_url):
    if check_json(data):
        applicants = Applicants()
        applicants.contact_id = data['vacancy']
        applicants.full_name = data['full_name']
        applicants.phone = data['phone']
        applicants.email = data['email']
        applicants.comment = data['comment']
        applicants.file = file_url
        applicants.save()
        return True
    else:
        return False


def get_context():
    company_data = get_queryset_company()
    vacancy_data = get_queryset_vacancy()
    contacts_data = get_contacts()
    data = {
        "company": company_data,
        "vacancy": vacancy_data,
        "contacts": contacts_data,
    }
    return data

