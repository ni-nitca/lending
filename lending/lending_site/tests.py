from django.test import TestCase
from lending_site.service import (
    get_queryset_company,
    get_queryset_vacancy,
    )
from lending_site.models import (
    Company,
    Contacts,
    Vacancy,
    Applicants
)


class ServiceTestCase(TestCase):
    company  = Company()
    contact = Contacts()
    company.name = 'xxx'
    company.description = 'xxxx'
    contact.adress = 'xxxxx'
    contact.phone = '314141'
    contact.email = '12345@gmail.com' 
    def test_gqc(self):
        print(get_queryset_company)

    def test_gqv(self):
        print(get_queryset_vacancy)