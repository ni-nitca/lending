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
    @classmethod
    def setUpTestData(cls):
        cls.c_name = 'Test'
        cls.c_description = 'Testing'
        cls.c_image = 'default.png'
        cls.v_name = 'Test2'
        cls.v_description = 'Testing2'
        cls.salary = '300-400'
        cls.activated = 'True'
        cls.pk = 1


        Company.objects.create(
          name=cls.c_name,
          description=cls.c_description,
          image=cls.c_image
        )

        Vacancy.objects.create(
            id = cls.pk,
            v_name = cls.v_name,
            description = cls.v_description,
            salary = cls.salary,
            activated = cls.activated
        )


    def test_cquery_is_true(self):
        valid_dict = {
          "name": self.c_name,
          "description": self.c_description,
          "image": self.c_image
        }
        invalid_dict = {
            "description": self.c_description,
            "image": 'pnx',
            "name": self.c_name,
        }
        company_queryset = get_queryset_company()
        self.assertEqual(company_queryset, valid_dict, msg=company_queryset)
        self.assertNotEqual(company_queryset, invalid_dict, msg=company_queryset)

    def test_vquery_is_true(self):
        valid_dict = {
        'name':self.v_name,
        'id':self.pk,
        'salary':self.salary,
        'description':self.v_description,
        }
        invalid_dict = {
        'name':self.v_name,
        'id':2,
        'salary':self.salary,
        'description':self.v_description,
        }
        vacancy_queryset = get_queryset_vacancy()
        print(vacancy_queryset)
        self.assertEqual(vacancy_queryset, valid_dict, msg=vacancy_queryset)
        self.assertNotEqual(vacancy_queryset, invalid_dict, msg=vacancy_queryset)
    


    
