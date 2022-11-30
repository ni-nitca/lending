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
    @classmethod
    def setUpTestData(cls):
        company  = Company()
        contact = Contacts()
        cls.c_name = 'xxx'
        cls.description = 'xxxx'
        cls.adress = 'xxxxx'
        cls.phone = '314141'
        cls.email = '12345@gmail.com'
        cls.phone = '12345'

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/index/')
        self.assertEqual(resp.status_code, 200)


    
